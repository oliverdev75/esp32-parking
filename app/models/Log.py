from dataclasses import dataclass
from datetime import datetime
from app import db


@dataclass
class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    vehicle = db.relationship('Vehicle', backref='logs')
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    entry_date = db.Column(db.DateTime, default=datetime.now())
    exit_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.to_dict(),
            'entry_date': self.entry_date,
            'exit_date': self.exit_date,
        }