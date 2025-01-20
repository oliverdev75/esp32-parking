from app import app, db
from app.models.User import User
import bcrypt
import datetime

user = User(
    email="luke@mail.com",
    fullname="Luke Skywalker",
    contact=649339154,
    created_at=datetime.datetime.now(),
    role_id=1,
    password = bcrypt.hashpw(
        'P@ssw0rd'.encode('utf-8'),
        bcrypt.gensalt()
    )
)

with app.app_context():
    db.session.add(user)
    db.session.commit()
    db.session.close()