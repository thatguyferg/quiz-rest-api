import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.environ['TEST_DB_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

TESTING = True