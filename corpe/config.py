import os

class Config(object):
    SECRET_KEY = '\x7f\xa4\x04\xa3b9\\\x07=\x91\xc5\xea\xf4Z\x94\xa2\xcb\xa1\x1f\x85\x8d\xcd<@'
    # SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/corpe'
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')