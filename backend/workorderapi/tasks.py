"""
tasks.py
- taks to be handled by redis
- all of these functions are called from flask but run in redis

Check database to see if file had already been scanned

"""

from workorderapi.scan import scan
from workorderapi.excel_pdf import Spreadsheet
from rq import get_current_job
from pathlib import Path

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
    return True


def add_file(file):
    global job
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

            job.meta['folder'] = result.parts[4]
            job.meta['path'] = result.as_posix()
            job.meta['name'] = result.name
            job.meta['ext'] = result.suffix

            set_status('Done')
        except KeyError:
            set_status('Not Found')
    except Exception:
        set_status('Something Went Wrong')
        set_status('Error')
