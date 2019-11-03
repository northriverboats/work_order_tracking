"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from flask import Blueprint  # , current_app
from flask_restful import Resource, reqparse

api = Blueprint('api', __name__)

parser = reqparse.RequestParser()
parser.add_argument('name')


class TodoItem(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}


class File(Resource):
    def post(self):
        args = parser.parse_args()
        name = args['name']
        # print(current_app.task_queue)
        return {'msg': 'Scanning for ' + name}


class FileStatus(Resource):
    def post(self):
        args = parser.parse_args()
        name = args['name']
        return {'status': 'Still scanning for ' + name}
