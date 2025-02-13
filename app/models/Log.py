from sqlalchemy import Integer, String, DateTime
from dataclasses import dataclass
from app import db


@dataclass
class Log(db.Model):
    __tablename__ = 'logs'

    id = db.Column(Integer, primary_key=True)
    created_at = db.Column(DateTime)
    user = db.relationship('User', backref='logs', lazy='dynamic')
    entry_date = db.Column(DateTime)
    exit_date = db.Column(DateTime)
