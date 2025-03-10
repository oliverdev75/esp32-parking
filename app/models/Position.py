from sqlalchemy import Integer, String, DateTime, Boolean
from dataclasses import dataclass
from app import db
from datetime import datetime, time
from .Reservation import Reservation


@dataclass
class Position(db.Model):
    __tablename__ = 'positions'

    id = db.Column(Integer, primary_key=True)
    created_at = db.Column(DateTime)
    code = db.Column(String(10), unique=True, nullable=False)
    busy = db.Column(Boolean, default=False)
    reservations = db.relationship("Reservation", backref='position')

    def is_reserved(self):
        for reservation in self.reservations:
            date_f = datetime.strftime(reservation.date, "%d/%m/%Y")
            now_f = datetime.strftime(datetime.now().date(), "%d/%m/%Y")
            if date_f > now_f:
                return True
        return False

    def last_reservation(self):
        for reservation in self.reservations:
            date_f = datetime.strftime(reservation.date, "%d/%m/%Y")
            now_f = datetime.strftime(datetime.now().date(), "%d/%m/%Y")
            if date_f > now_f:
                return reservation