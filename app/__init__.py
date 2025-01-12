from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from .models import *
from os import environ
import secrets

app = Flask(__name__)

connection_string = f"{environ.get('DB_CONNECTION')}://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOST')}:{environ.get('DB_PORT')}/{environ.get('DB_NAME')}"
app.config.update(
    SECRET_KEY=secrets.token_hex(16),
    SESSION_PERMANENT=False,
    SESSION_TYPE="sqlalchemy",
    SQLALCHEMY_DATABASE_URI=connection_string
)

Bootstrap(app)

db = SQLAlchemy(app)
Session(app)
with app.app_context():
    session.app.session_interface.db.create_all()

from .auth import routes