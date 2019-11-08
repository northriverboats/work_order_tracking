"""
tasks.py
- taks to be handled by redis
- all of these functions are called from flask but run in redis
"""

# from Flask import current_app
# from workorderapi.application import create_app
# from workorderapi.models import db, Workorder, History
from workorderapi.scan import scan
from workorderapi.excel_pdf import Spreadsheet
from rq import get_current_job

job = None


def set_status(message):
    if job:
        job.meta['status'] = message
        job.save_meta()
    else:
        print(message)


def add_file(file):
    global job
    job = get_current_job()

    set_status('Scanning')
    files = scan()
    set_status('Scan complete')
    try:
        result = files[file]

        sheet = Spreadsheet(result, job)
        sheet.proccess_sheet()

        job.meta['folder'] = result.parts[4]
        job.meta['path'] = result.as_posix()
        job.meta['name'] = result.name
        job.meta['ext'] = result.suffix

        set_status('Done')
    except KeyError:
        set_status('Not Found')
