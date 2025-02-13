from .. import app
from .. import db
from ..models.User import User
from flask import render_template, redirect, url_for, session
from app.forms.LoginForm import LoginForm
import bcrypt

@app.route('/')
def index():
    return redirect(url_for('floor1'))

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
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                session['user'] = user
                return redirect(url_for('floor1'))
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
        message_type=message_type
    )

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))