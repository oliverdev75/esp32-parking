from sqlalchemy import Integer, DateTime
from dataclasses import dataclass
from app import db
from .User import User
from .Position import Position

@dataclass
class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(Integer, primary_key=True)
    created_at = db.Column(DateTime)
    user = db.relationship(User, backref='reservations', lazy='dynamic')
    position = db.relationship(Position, backref='reservations', lazy='dynamic')

    def __repr__(self):
        return f"<Reservation {self.user.email}, {self.position.code}, {self.created_at}>"

