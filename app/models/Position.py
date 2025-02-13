from sqlalchemy import Integer, String, DateTime
from dataclasses import dataclass
from app import db


@dataclass
class Position(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(Integer, primary_key=True)
    created_at = db.Column(DateTime)
    code = db.Column(String(10), unique=True, nullable=False)
    floor = db.Column(Integer, nullable=False)
    