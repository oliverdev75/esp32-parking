from datetime import timedelta
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from .models import *
import os, secrets

load_dotenv()

app = Flask(__name__)
connection_string = f"{os.getenv('DB_CONNECTION')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
app.config.update(
    SECRET_KEY=secrets.token_hex(16),
    SESSION_PERMANENT=True,
    PERMANENT_SESSION_LIFETIME=timedelta(days=31),
    SQLALCHEMY_DATABASE_URI=connection_string
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)

from . import console
from .routes import parking, vehicle,  auth, api

