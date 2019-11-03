"""
config.py
- settings for the flask application object
"""
import os


class BaseConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///workorder.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # used for encryption and session management
    SECRET_KEY = 'mysecretkeybooger!!!'
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
