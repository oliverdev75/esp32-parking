from sqlalchemy import Integer, String
from datetime import datetime
from app import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    plate_number = db.Column(Integer, nullable=False)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    reservations = db.relationship("Reservation", backref="vehicle")

    def to_dict(self):
        return {
            'id': self.id,
            'plate_number': self.plate_number,
            'user': self.user.to_dict(vehicle=False),
        }

    def has_reservation(self):
        result = False
        for reservation in self.reservations:
            date_f = datetime.strftime(reservation.date, "%d/%m/%Y")
            now_f = datetime.strftime(datetime.today(), "%d/%m/%Y")
            if date_f > now_f:
                print("In func: ", date_f > now_f)
                result = True
        return result