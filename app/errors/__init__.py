from flask import Blueprint

bp = Blueprint('errors', __name__)  # 2nd - is the name of the base module of the bp

from app.errors import handlers
