from sqlalchemy import Integer, String
from .. import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(Integer, primary_key=True)
    role = db.Column(String(255), nullable=False)

    def __init__(
        self,
        role
    ):
        super().__init__()
        self.role = role