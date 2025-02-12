from .. import app
from .. import db
from ..decorators import logged
from ..models.User import User
from flask import render_template, redirect, url_for, session
from app.forms.LoginForm import LoginForm
import bcrypt

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
                message = "Successfuly loged in!"
                message_type = "success"
            else:
                message = "Password wrong!"
                message_type = "danger"
        else:
            message = "User doesn't exist!"
            message_type = "danger"


    return render_template(
        'login.html',
        form=form,
        username=user.fullname if user else None,
        message=message,
        message_type=message_type
    )

@app.route('/logout')
@logged
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/parking1', methods=['GET', 'POST'])
def parking1():
    return render_template("parking-1.html")

@app.route('/parking2', methods=['GET', 'POST'])
def parking2():
    return render_template("parking-2.html")
