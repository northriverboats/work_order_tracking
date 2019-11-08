"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint, current_app
from flask_restful import Resource, reqparse


api = Blueprint('api', __name__)

parser_file = reqparse.RequestParser()
parser_file.add_argument('name')

parser_file_status = reqparse.RequestParser()
parser_file_status.add_argument('job')


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}


class File(Resource):
    def post(self):
        args = parser_file.parse_args()
        name = args['name']
        job = current_app.task_queue.enqueue(
            'workorderapi.tasks.add_file', name)
        job.meta['status'] = 'Started'
        job.save_meta()
        return {'job': job.get_id()}


class FileStatus(Resource):
    def post(self):
        args = parser_file_status.parse_args()
        job_id = args['job']
        job = current_app.task_queue.fetch_job(job_id)
        if job:
            job.refresh()
            meta = job.meta
        else:
            meta = []
            meta['status'] = 'Done'

        return {'status': meta['status']}
