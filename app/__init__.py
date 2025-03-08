from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os, secrets
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
connection_string = f"{os.getenv('DB_CONNECTION')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config.update(
    SECRET_KEY=secrets.token_hex(16),
    SESSION_PERMANENT=False,
    SESSION_TYPE="filesystem",
    SQLALCHEMY_DATABASE_URI=connection_string
)

db = SQLAlchemy(app)

from .models import *

migrate = Migrate(app, db)

Bootstrap(app)

from . import console
from .routes import parking, auth, api

