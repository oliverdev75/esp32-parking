from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from os import environ
import secrets
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
connection_string = f"{environ.get('DB_CONNECTION')}://{environ.get('DB_USER')}:{environ.get('DB_PASSWORD')}@{environ.get('DB_HOST')}:{environ.get('DB_PORT')}/{environ.get('DB_NAME')}"
app.config.update(
    SECRET_KEY=secrets.token_hex(16),
    SESSION_PERMANENT=False,
    SESSION_TYPE="sqlalchemy",
    SQLALCHEMY_DATABASE_URI=connection_string
)

db = SQLAlchemy(app)

from .models import *

migrate = Migrate(app, db)

Bootstrap(app)

from . import console
from .reservation import routes
from .auth import routes
