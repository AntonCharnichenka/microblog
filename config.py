import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_VALUE = 'lolkek'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or DEFAULT_VALUE
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///{}'.format(os.path.join(BASEDIR, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATION = False
