from sqlalchemy import Integer, String, DateTime, ForeignKey, text
from sqlalchemy.orm import declared_attr
from dataclasses import dataclass
from .. import app, db
from .Role import Role

@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    created_at = db.Column(DateTime)
    email = db.Column(String(255), unique=True, nullable=False)
    password = db.Column(String(255), nullable=False)
    fullname = db.Column(String(255), nullable=False)
    contact = db.Column(Integer, nullable=False)
    role_id = db.Column(Integer, ForeignKey(Role.id), nullable=False)

    @declared_attr
    def role(self):
        role_name = None
        query = text("SELECT * FROM roles WHERE id = :role_id")
        with app.app_context():
            role_name = db.session.execute(query, params=dict(role_id = self.role_id)).fetchall()
        return role_name
    
    def getAttributes(self):
        return self.__dict__