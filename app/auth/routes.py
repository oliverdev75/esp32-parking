from .. import app
from .. import db
from ..models.User import User
from flask import url_for
from flask import render_template, redirect, session
from ..forms.LoginForm import LoginForm
from ..forms.RegisterForm import RegisterForm
import bcrypt

@app.route('/')
def root():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = None
    message = None
    message_type = None
    if form.validate_on_submit():
        form_email = form.email.data
        password = form.password.data
        user = db.session.query(User).filter_by(email = form_email).first()
        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                session['user'] = user
                return redirect('parking')
            else:
                message = "Password wrong!"
                message_type = "danger"
        else:
            message = "User doesn't exist!"
            message_type = "danger"

    return render_template(
        'login.html',
        form=form,
        page='login',
        username=user.fullname if user else None,
        message=message,
        message_type=message_type
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    from datetime import datetime

    form = RegisterForm()

    if form.validate_on_submit():
        fullname = form.name.data
        email = form.email.data
        password = form.password.data
        password_confirm = form.repeat_password.data
        contact_number = form.contact.data
        car_plate = form.car_plate.data

        message = None

        user = db.session.query(User).filter_by(email=email).first()
        number_plate = db.session.query(User).filter_by(car_plate=car_plate).first()

        if user:
            message = "User already exists!"
        elif password != password_confirm:
            message = "The passwords must match!"
        elif len(str(contact_number)) < 9:
            message = "The contact number must be at least 8 digits!"
        elif number_plate:
            message = "The plate already exist!"

        if message:
            return render_template('register.html',form=form,message=message, message_type='danger')
        else:

            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

            user = User(
                email = email,
                password = hashed_password,
                fullname = fullname,
                contact = int(contact_number),
                car_plate = car_plate,
                role_id = 1,
                created_at = datetime.now(),
            )

            page = None

            try:
                with app.app_context():
                    db.session.add(user)
                    db.session.commit()
                    message = 'User created!'
                    message_type = 'success'
                    page = 'login'
                    return  redirect(page)

            except Exception as e:
                db.session.rollback()
                message='User cannot be registered, please contact the administrator'
                message = e
                message_type='danger'
                page = 'register'

            return render_template(page+'.html', form=form, page='register',message=message, message_type=message_type)

    return render_template('register.html',form=form, page='register',)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/parking1', methods=['GET', 'POST'])
def parking1():
    return render_template("parking-1.html")

@app.route('/parking2', methods=['GET', 'POST'])
def parking2():
    return render_template("parking-2.html")
