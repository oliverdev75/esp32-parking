from sqlalchemy import Integer, String
from app import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(Integer, primary_key=True)
    role = db.Column(String(255), nullable=False)
    users = db.relationship("User", back_populates="role")

    def __repr__(self):
        return self.role