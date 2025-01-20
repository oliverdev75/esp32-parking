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

def dbInsert(data: list):
    with app.app_context():
        db.session.add_all(data)
        db.session.commit()



def createUser(data: dict):
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


def seedFiles():
    users = []
    for seeder in os.listdir("seeders"):
        with open(seeder,'r') as data:
            for model in csv.reader(data):
                users.append(
                    createUser({
                        "email": model[0],
                        "password": model[1],
                        "fullname": model[2],
                        "contact": model[3],
                        "role_id": model[4],
                    })
                )
    dbInsert(users)


def seedUsersFile():
    users = []
    try:
        with open(USERS_DATA_FILE,'r') as data:
            for model in csv.reader(data):
                users.append(
                    createUser({
                        "email": model[0],
                        "password": model[1],
                        "fullname": model[2],
                        "contact": model[3],
                        "role_id": model[4],
                    })
                )
    except Exception as error:
        print(error)
    dbInsert(users)


def seedUser():
    data = {}
    data["email"] = input("Email: ")
    data["password"] = getpass()
    data["fullname"] = input("Fullname: ")
    data["contact"] = input("Contact: ")
    data["role"] = input("Role: ")
    with app.app_context():
        data["role_id"] = db.session.query(Role).filter(Role.role == data['role']).first().id
    dbInsert([createUser(data)])


def updateUserPassword():
    filterChoice = int(input("Email (1) or id (2): "))
    filteremail = None
    if filterChoice == 1:
        filter = input("Email: ")
    else:
        filter = int(input("id: "))
    
    password = getpass()
    query = None
    with app.app_context():
        if filterChoice == 1:
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



try:
    match sys.argv[1]:
        case "migrate":
            migrate()
        case "seed:files":
            seedFiles()
        case "seed:users":
            seedUsersFile()
        case "seed:user":
            seedUser()
        case "update:password":
            updateUserPassword()
        case _:
            print(f"Unknown command \"{sys.argv[1]}\"")
except Exception:
    print("You must provide an action: migrate, seed...")