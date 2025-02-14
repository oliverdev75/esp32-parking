from crypt import methods
from datetime import timezone

from .. import app
from .. import db
from ..models.User import User
from flask import render_template, redirect, request, session, make_response, flash
from .LoginForm import LoginForm
import bcrypt

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
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
    
    if message:
        if user:
            return render_template(
                'login.html',
                form=form,
                user_ip=user_ip,
                username=user.fullname,
                message=message,
                message_type=message_type
            )
        else:
            return render_template(
                'login.html',
                form=form,
                user_ip=user_ip,
                message=message,
                message_type=message_type
            )
    return render_template(
                'login.html',
                form=form,
                user_ip=user_ip,
            )

@app.route('/entrada', methods=['POST'])
def entrada():
    data = request.get_json(force=True)

    matricula = data.get('matricula')

    registro = User.filter_by(matricula=matricula).first()

    if  not registro:
        return  jsonify({"error": "Matricula no registrada"}), 403
    else:
        return  'Matricula existente'

    spot = ParkingSpot.query.filter_by(free=False).first()

    if spot:
        new_log = ParkingLog(
            car_plate = matricula,
            entry_time = datetime.now(utc)
        )
        db.session.add(new_log)
        db.session.commit()
        return  jsonify({
            "message": "Welcome to Bernat",
            "plate": matricula,
            "entry_time":  entry_time
        }), 200
    else
        return  jsonify({"error": "No hay sitios disponibles"}), 409

@app.route('/updateSpot', methods=['POST'])
def updateSpot()
    data = request.get_json(force=True)
    spotID = data.get('spotID')
    state = data.get('state')

    spot = parkingSpot.query.filter_by(id=spotID).first()

    spot.is_ocupet = state


    db.session.commit()

    return jsonify({
        "message": "spot updated",
        "spot": spotID,
        "state": state
    }), 200
