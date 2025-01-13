from sqlalchemy import Integer, String, DateTime, ForeignKey, text
from sqlalchemy.orm import declared_attr, relationship
from .. import app, db
from .Role import Role
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    created_at = db.Column(DateTime)
    email = db.Column(String(255), unique=True, nullable=False)
    password = db.Column(String(255), nullable=False)
    fullname = db.Column(String(255), nullable=False)
    contact = db.Column(Integer, nullable=False)
    role_id = db.Column(String, ForeignKey(Role.id), nullable=False)

    """ @declared_attr
    def role(self):
        role_name = None
        query = text(f"SELECT * FROM roles WHERE id = :role")
        with app.app_context():
            role_name = db.session.execute(query, params=dict(role=self.role_id))
        return role_name """