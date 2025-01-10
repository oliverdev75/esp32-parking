from flask import Flask
from .setup import database
import config as config

app = Flask(__name__)

db_string = f"{config.DB_CONNECTION}://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
app.config["SQLALCHEMY_DATABASE_URI"] = db_string

database.db.init_app(app)