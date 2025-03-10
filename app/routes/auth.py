from app import app
from app import db
from app.forms.RegisterForm import RegisterForm
from app.models.User import User
from app.models.Role import Role
from flask import render_template, redirect, url_for, session, make_response
from app.forms.LoginForm import LoginForm
from app.models.Vehicle import Vehicle
import bcrypt

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    message = None
    message_type = None
    if form.validate_on_submit():
        form_email = form.email.data
        password = form.password.data
        user = db.session.query(User).filter_by(email = form_email).first()
        if user:
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                session['user'] = user.id
                res = redirect(url_for('index'))
                return res
            else:
                message = "Password wrong!"
                message_type = "danger"
        else:
            message = "User doesn't exist!"
            message_type = "danger"


    return render_template(
        'login.html',
        form=form,
        message=message,
        message_type=message_type,
        logged=False
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user' in session:
        return redirect(url_for('parking_page'))
    form = RegisterForm()
    if form.validate_on_submit():
        form_email = form.email.data
        user = db.session.query(User).filter_by(email = form_email).first()
        password = form.password.data
        repeat_password = form.repeat_password.data
        if user:
            return render_template('register.html',
               message="User already exists!",
               message_type="danger"
            )

        if password != repeat_password:
            return render_template('register.html',
               message="Passwords don't match!",
               message_type="danger"
            )
        name = form.name.data
        fullname = form.fullname.data
        contact = form.contact.data
        car_name = form.car_name.data
        car_plate = form.car_plate.data
        role_id = db.session.query(Role).filter_by(role = 'client').first().id
        user = User(
            email=form_email,
            name=name,
            password=password,
            fullname=fullname,
            contact=contact,
            role_id=role_id
        )
        vehicle = Vehicle(name=car_name, plate_number=car_plate)
        user.vehicles.append(vehicle)
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))