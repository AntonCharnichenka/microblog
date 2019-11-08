from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db_migration_engine = Migrate(app, db)

from app import routes, models  # TODO: add this error ignoring
