from flask import render_template, redirect, url_for, session, request
from datetime import datetime, timedelta
from app import app, db
from app.models.User import User
from app.models.Vehicle import Vehicle
from app.models.Position import Position
from app.models.Reservation import Reservation

@app.route('/')
def index():
    return redirect(url_for('parking_page'))

@app.route('/parking', methods=['GET', 'POST'])
def parking_page():
    if 'user' not in session:
        return redirect(url_for('login'))
    position_id = request.args.get('position')
    specified_position = None
    active_position = ''
    user_position = None
    vehicle_position = None
    if position_id:
        specified_position = db.session.query(Position).filter_by(code = position_id).first()
        if specified_position.is_reserved():
            active_position = "active-reserved"
            vehicle_position = specified_position.last_reservation().vehicle
            user_position = vehicle_position.user
        elif specified_position.busy:
            active_position = "active-busy"
        else:
            active_position = "active-available"
    positions = db.session.query(Position).all()
    return render_template('parking.html',
       specified_position=specified_position,
       vehicle_position=vehicle_position,
       user_position=user_position,
       active_position=active_position,
       positions=positions,
       user=db.session.query(User).filter_by(id = session['user']).first(),
       error=session.get('error'),
    )

@app.route('/position/reservate', methods=['POST'])
def reservate():
    if 'user' not in session:
        return redirect(url_for('login'))
    position_id = request.form.get('position')
    vehicle_id = request.form.get('vehicle')
    vehicle = db.session.query(Vehicle).filter_by(id = vehicle_id).first()
    reservation_date = datetime.today() + timedelta(days=1)
    all_reserved = True
    user = db.session.query(User).filter_by(id = session['user']).first()
    for vehicle in user.vehicles:
        if not vehicle.has_reservation():
            all_reserved = False
    print("Out func: ",vehicle.has_reservation())
    if all_reserved or vehicle.has_reservation():
        session['error'] = "All your vehicles have reserved positions."
        return redirect(url_for('parking_page'))
    db.session.add(
        Reservation(
            position_id=position_id,
            vehicle_id=vehicle_id,
            date=reservation_date
        )
    )
    db.session.commit()
    return redirect(url_for('parking_page'))