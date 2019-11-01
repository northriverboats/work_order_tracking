"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask


def create_app(app_name='WORKORDER_API'):
    app = Flask(app_name)
    app.config.from_object('workorderapi.config.BaseConfig')
    from workorderapi.api import api
    app.register_blueprint(api, url_prefix="/api")
    return app
