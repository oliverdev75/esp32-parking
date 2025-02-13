#!/bin/env python3

from app import app, db
from app.models.User import User
from app.models.Role import Role
import os, csv, bcrypt, datetime
from getpass import getpass

def db_insert(data: list):
    with app.app_context():
        db.session.add_all(data)
        db.session.commit()


def create_user(data: dict):
    return User(
        email=data['email'],
        password=bcrypt.hashpw(
            data['password'].encode('utf-8'),
            bcrypt.gensalt()
        ),
        fullname=data['fullname'],
        contact=int(data['contact']),
        role_id=int(data['role_id']),
        created_at=datetime.datetime.now()
    )

@app.cli.command('seed:files')
def seed_files():
    users = []
    for seeder in os.listdir("seeders"):
        with open(seeder,'r') as data:
            for model in csv.reader(data):
                users.append(
                    create_user({
                        "email": model[0],
                        "password": model[1],
                        "fullname": model[2],
                        "contact": model[3],
                        "role_id": model[4],
                    })
                )
    db_insert(users)


@app.cli.command('create:user')
def seed_user():
    data = {
        "email": input("Email: "),
        "password": getpass(),
        "fullname": input("Fullname: "),
        "contact": input("Contact: "),
        "role": input("Role: ")
    }
    with app.app_context():
        data["role_id"] = db.session.query(Role).filter(Role.role == data['role']).first().id
    db_insert([create_user(data)])


@app.cli.command('user:password')
def update_user_password():
    filter_choice = int(input("Email (1) or id (2): "))
    if filter_choice == 1:
        filter = input("Email: ")
    else:
        filter = int(input("id: "))

    password = getpass()
    with app.app_context():
        if filter_choice == 1:
            query = db.session.query(User).filter(User.email == filter)
        else:
            query = db.session.query(User).filter(User.id == filter)

        query.update({
            User.password: bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            )
        })
        db.session.commit()