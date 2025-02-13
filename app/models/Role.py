from sqlalchemy import Integer, String
from app import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(Integer, primary_key=True)
    role = db.Column(String(255), nullable=False)