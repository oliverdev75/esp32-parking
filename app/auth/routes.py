from .. import app
from ..models import User
from flask import render_template, redirect, request, session, make_response, flash
from .LoginForm import LoginForm
import bcrypt

@app.route('/', methods=['GET', 'POST'])
def login():
    user = None
    user_ip = ''
    if 'user_ip' in request.cookies:
        user_ip = request.cookies.get('user_ip')
        if 'user' in session:
            user = session.get('user')
    else:
        session.clear()
        res = make_response(redirect('/'))
        res.set_cookie('user_ip', request.remote_addr)
        flash("Session closed, log in please.")
        return res

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter(User.email == email).first()
        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user.password):
                session['user'] = user
                return render_template('information.html', form=form, message="Successfuly loged in!")
            else:
                return render_template('information.html', form=form, message="Password wrong!")
        else:
            return render_template('information.html', form=form, message="User doesn't exist!")
        
    return render_template('information.html', form=form)