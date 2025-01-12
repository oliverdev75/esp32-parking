from sqlalchemy import Integer, String, DateTime
from .. import db
from datetime import datetime
import bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    created_at = db.Column(DateTime)
    email = db.Column(String(255), unique=True, nullable=False)
    password = db.Column(String(255), nullable=False)
    fullname = db.Column(String(255), nullable=False)
    contact = db.Column(Integer, nullable=False)
    role = db.Column(String, nullable=False)

    def __init__(
            self,
            email,
            password,
            fullname,
            surnames,
            contact,
            role,
    ):
        super().__init__()
        self.email = email
        self.fullname = fullname
        self.surnames = surnames
        self.contact = contact
        self.role = role
        self.created_at = datetime.now()
        self.password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )