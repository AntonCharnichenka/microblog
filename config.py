import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_VALUE = 'lolkek'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or DEFAULT_VALUE

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///{}'.format(os.path.join(BASEDIR, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATION = False

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or '25')
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['waitforyourletter@gmail.com']
