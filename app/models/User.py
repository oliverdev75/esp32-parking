from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import declared_attr
from dataclasses import dataclass
from .. import app, db

@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer(), primary_key=True)
    created_at = db.Column(DateTime())
    email = db.Column(String(255), unique=True, nullable=False)
    password = db.Column(String(255), nullable=False)
    fullname = db.Column(String(255), nullable=False)
    contact = db.Column(Integer(), nullable=False)
    role_id = db.Column(db.ForeignKey("roles.id"))
    role = db.relationship("Role", back_populates="users")
    vehicles = db.relationship("Vehicle", back_populates="user")

    def to_dict(self, vehicle=True):
        data = { 'email': self.email, 'role': self.role.role, 'fullname': self.fullname, 'contact': self.contact }
        if vehicle:
            data['vehicles'] = [vehicle.to_dict() for vehicle in self.vehicles]
        return data

    def __repr__(self):
        return f"<User {self.email}, {self.role}, {self.fullname}, {self.contact}, {self.vehicles}>"