import os
from constants import SECRET_KEY, PASSWORD_SALT, DATABASE_URI


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get(SECRET_KEY) or os.urandom(32)
    SECURITY_PASSWORD_SALT = os.environ.get(PASSWORD_SALT) or os.urandom(32)
    SQLALCHEMY_DATABASE_URI = os.environ.get(DATABASE_URI)


class ProductionConfig(BaseConfig):
    DEBUG = False


class StagingConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
