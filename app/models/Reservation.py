from sqlalchemy import DateTime
from dataclasses import dataclass
from app import db

@dataclass
class Reservation(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.ForeignKey('vehicles.id'), primary_key=True)
    position_id = db.Column(db.ForeignKey('positions.id'), primary_key=True)
    created_at = db.Column(DateTime)

    def __repr__(self):
        return f'<Reservation {self.vehicle_id}, {self.position_id}, {self.created_at}>'

    def to_dict(self):
        return {
            'vehicle_id': self.vehicle_id,
            'position_id': self.position_id,
            'created_at': self.created_at,
        }