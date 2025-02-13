#!/bin/env python3

from app import app, db
from app.models.User import User
from app.models.Role import Role
from migrations.migrations import migrate
import sys, os, csv, bcrypt, datetime
from getpass import getpass

'''
    This is NOT the entrypoint of the app please to
    run it execute in the terminal: flask run
'''

USERS_DATA_FILE = 'seeders/users.csv'

def db_insert(data: list):
    with app.app_context():
        db.session.add_all(data)
        db.session.commit()

def dbInsertUser(data: list):
    with app.app_context():
        db.session.add(data)
        db.session.commit()

def create_user(data: dict):
    return User(
        email=data['email'],
        password = bcrypt.hashpw(
            data['password'].encode('utf-8'),
            bcrypt.gensalt()
        ),
        fullname=data['fullname'],
        contact=int(data['contact']),
        role_id=int(data['role_id']),
        created_at=datetime.datetime.now()
    )


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
                        "car_plate": model[4],
                        "role_id": model[5],
                    })
                )
    db_insert(users)


def seed_users_file():
    users = []
    try:
        with open(USERS_DATA_FILE,'r') as data:
            for model in csv.reader(data):
                users.append(
                    create_user({
                        "email": model[0],
                        "password": model[1],
                        "fullname": model[2],
                        "contact": model[3],
                        "car_plate": model[4],
                        "role_id": model[5],
                    })
                )
    except Exception as error:
        print(error)
    db_insert(users)


def seedUser():
    data = {}
    data["email"] = input("Email: ")
    data["password"] = getpass()
    data["fullname"] = input("Fullname: ")
    data["contact"] = input("Contact: ")
    data["car_plate"] = input("Car plate: ")
    data["role"] = input("Role: ")
    with app.app_context():
        data["role_id"] = db.session.query(Role).filter(Role.role == data['role']).first().id
    db_insert([create_user(data)])


def updateUser():
    id = int("Id: ")
    

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

def freshDB():
    with app.app_context():
        db.drop_all()
        db.create_all()

try:
    match sys.argv[1]:
        case "migrate":
            migrate()
        case "migrate:fresh":
            freshDB()
        case "seed:files":
            seed_files()
        case "seed:users":
            seed_users_file()
        case "seed:user":
            seedUser()
        case "update:password":
            update_user_password()
        case _:
            print(f"Unknown command \"{sys.argv[1]}\"")
except Exception:
    print("You must provide an action: migrate, seed...")