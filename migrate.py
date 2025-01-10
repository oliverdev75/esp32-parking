from app import app
from app.setup.database import db

with app.app_context():
    db.create_all()