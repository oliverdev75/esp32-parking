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

@app.route('/parking1', methods=['GET', 'POST'])
def func():
    parking_count = 15
    parking_width = 48
    total_width = parking_count * parking_width
    offset = total_width / 2
    topOffset = 16
    totalVerticalDisplacement = 84
    vertical_positions = [((abs(parking_count - i) * (totalVerticalDisplacement / parking_count)) + topOffset) for i in range(parking_count)]
    horizontal_positions = [(i * (parking_width + 8)) + offset for i in range(parking_count)]
    return render_template("parking_p1.html", 
                           horizontal_positions=horizontal_positions, 
                           parking_count=parking_count, 
                           parking_width=parking_width, 
                           vertical_positions=vertical_positions
                           )
