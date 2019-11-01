#!/usr/bin/python3

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/opt/workordertracking/backend/")

from application import create_app
application = create_app()
