"""
scan.py
- build list of xls/xlsx sheets in the Boats Production Folders
"""

from pathlib import Path
import time
from rq import get_current_job


job = None


def set_status(message):
    if job:
        text = job.meta['status']
        job.meta['status'] = text + message + '\n'
        job.save_meta()
    else:
        print(message)


def scan():
    global job
    job = get_current_job()
    skip = [
        'Delivered Boats 2008',
        'Delivered Boats 2009',
        'Delivered Boats 2010',
        'Delivered Boats 2011',
        'Delivered Boats 2012',
        'Delivered Boats 2013',
        'Delivered Boats 2014',
        'Delivered Boats 2015',
        'Delivered Boats 2016',
        'Delivered Boats 2017',
    ]

    dir = Path(r'/samba/shares/production/Boats Waiting Production/')
    bwp = {}
    set_status('Scanning: {}'.format(dir.name))
    for file in dir.glob('**/*.xls*'):
        bwp[file.name] = file

    dir = Path(r'/samba/shares/production/Boats In Production/')
    bip = {}
    set_status('Scanning: {}'.format(dir.name))
    for file in dir.glob('**/*.xls*'):
        bip[file.name] = file

    dir = Path(r'/samba/shares/production/Delivered Boats/')
    deb = {}
    for folder in dir.glob('Delivered*'):
        if folder.name not in skip:
            if job:
                set_status('Scanning: {}'.format(folder.name))
            for file in folder.glob('**/*.xls*'):
                deb[file.name] = file

    files = {**bwp, **bip, **deb}
    return files


def test():
    start_time = time.time()
    files = scan()
    print("--- %s seconds ---" % (time.time() - start_time))
    for file in files:
        print("{:24} {}".format(files[file].parts[4], files[file].name))
    print(len(files))


if __name__ == "__main__":
    test()
