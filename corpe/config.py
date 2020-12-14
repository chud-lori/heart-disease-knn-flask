"""
create class configuration
"""

# import os


class Config(object):
    """
    class Config
    """
    SECRET_KEY = '\x7f\xa4\x04\xa3b9\\\x07=\x91\xc5\xea\xf4Z\x94\xa2\xcb\xa1\x1f\x85\x8d\xcd<@'
    # SECRET_KEY = os.getenv('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/corpe'
    SQLALCHEMY_DATABASE_URI = 'postgres://yteqsluiclaqqf:a68ff5634a2c9998a11a0bdf8086a48a9cfba042c80acda300c0d991bd4c5d60@ec2-52-206-15-227.compute-1.amazonaws.com:5432/dbuu5r7mpfu1re'
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
