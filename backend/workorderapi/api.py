"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, current_app
from flask_restful import Resource, reqparse
from .db import Session
from .models import Workorder

api = Blueprint('api', __name__)

parser_file = reqparse.RequestParser()
parser_file.add_argument('name')
parser_file.add_argument('userid')


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}


class File(Resource):
    def post(self):
        args = parser_file.parse_args()
        name = args['name']
        user_id = args['userid']
        job = current_app.task_queue.enqueue(
            'workorderapi.tasks.add_file', name, user_id)
        job.save_meta()
        return {'job': job.get_id()}


class FileStatus(Resource):
    def get(self, job_id):
        job = current_app.task_queue.fetch_job(job_id)
        if job:
            job.refresh()
            meta = job.meta
            status = meta.get('status', '')
        else:
            return {'status': 'Done'}

        return {'status': status}


class WorkOrderHistory(Resource):
    def get(self, user_id):
        results = []
        for workorder in Session.query(Workorder).\
                order_by(Workorder.hull).\
                filter_by(archived=False, user_id=user_id):
            results.append({
                'id': workorder.id,
                'hull': workorder.hull,
                'workorder': workorder.workorder,
                'folder': workorder.folder,
                'found': workorder.found,
                'archived': workorder.archived
            })
            # results.append(workorder.to_dict())
        return {'workorders': results}
