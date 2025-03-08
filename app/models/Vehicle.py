from sqlalchemy import Integer, String
from app import db

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = db.Column(Integer, primary_key=True)
    plate_number = db.Column(Integer, nullable=False)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates="vehicles")
    reservations = db.relationship("Reservation", backref="vehicle")

    def to_dict(self):
        return {
            'id': self.id,
            'plate_number': self.plate_number,
            'user': self.user.to_dict(vehicle=False),
        }