"""
tasks.py
- taks to be handled by redis
- all of these functions are called from flask but run in redis

Check database to see if file had already been scanned

"""

from .scan import scan
from .excel_pdf import Spreadsheet
from .db import Session
from .models import User, Workorder, History
from rq import get_current_job
from pathlib import Path
import re

job = None


def set_status(message):
    if job:
        text = job.meta['status']
        job.meta['status'] = text + message + '\n'
        job.save_meta()
    else:
        print(message)


def sanity_check(file):
    file = Path(file)
    if Path('/opt/workorders_git/' + file.stem + '.txt').exists():
        set_status('File Is Already Being Tracked')
        set_status('Error')
        return False
    if not (file.suffix.lower() == '.xls' or file.suffix.lower() == '.xlsx'):
        set_status('File Is Not An Excel File')
        set_status('Error')
        return False
    match = re.search(r'\d{5} ?[A-L]\d{3}', file.name)
    if not match:
        set_status('File Name Does Not Contain  Hull Serial Number')
        set_status('Error')
        return False
    return True


def add_file(file, user_id):
    global job
    user = Session.query(User).filter_by(id=user_id).first()
    job = get_current_job()
    if job:
        job.meta['status'] = ''
        job.save_meta()

    try:
        if not sanity_check(file):
            return

        set_status('Adding File: {}'.format(file))

        set_status('Scanning')
        files = scan()
        set_status('Scan complete')
        try:
            result = files[file]

            sheet = Spreadsheet(result, job)
            sheet.proccess_sheet()

            if 'Error' in job.meta['status']:
                return

            match = re.search(r'\d{5} ?[A-L]\d{3}', result.name)
            # future home of database call
            hi = History(description='Added to tracking system')
            wo = Workorder(workorder=result.name,
                           hull=match.group(),
                           folder=result.parts[4],
                           history=[hi],
                           user_id=user.id)
            Session.add(hi)
            Session.add(wo)
            Session.commit()

            set_status('Done')
        except KeyError:
            set_status('Not Found')
    except Exception as e:
        set_status(str(e))
        set_status('Something Went Wrong')
        set_status('Error')
