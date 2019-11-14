"""
config.py
- settings for the flask application object
"""
import os
from distutils.util import strtobool


def envrion_tf(key):
    temp = strtobool(os.environ.get(key))
    return True if temp == 1 else False


class BaseConfig(object):
    DEBUG = envrion_tf('DEBUG')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = envrion_tf(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    REDIS_URL = os.environ.get('REDIS_URL')
    # used for encryption and session management
    SECRET_KEY = os.environ.get('SECRET_KEY')
