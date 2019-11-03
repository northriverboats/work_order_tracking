"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_restful import Api
from redis import Redis
import rq


def create_app(app_name='WORKORDER_API'):
    app = Flask(app_name)
    app.config.from_object('workorderapi.config.BaseConfig')

    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('workorder-tasks', connection=app.redis)

    from workorderapi.api import api, TodoItem, File, FileStatus
    my_api = Api(api)
    my_api.add_resource(TodoItem, '/todos/<int:id>')
    my_api.add_resource(File, '/file')
    my_api.add_resource(FileStatus, '/file/status')
    app.register_blueprint(api, url_prefix="/api")

    from workorderapi.models import db
    db.init_app(app)

    return app
