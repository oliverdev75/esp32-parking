from flask import render_template, redirect, url_for, session, request
from datetime import datetime, timedelta
from app import app, db
from app.decorators import auth, guest
from app.models.User import User
from app.models.Vehicle import Vehicle
from app.models.Position import Position
from app.models.Reservation import Reservation

@app.route('/')
@auth
def index():
    return redirect(url_for('parking_page'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notfound.html')

@app.route('/parking', methods=['GET', 'POST'])
@auth
def parking_page():
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
    busy_positions_quant = len(db.session.query(Position).filter_by(busy = True).all())
    busy_percentage = int((busy_positions_quant / len(positions)) * 100)
    return render_template('parking.html',
       specified_position=specified_position,
       vehicle_position=vehicle_position,
       user_position=user_position,
       active_position=active_position,
       positions=positions,
       busy_percentage=busy_percentage,
       user=db.session.query(User).filter_by(id = session['user']).first(),
       error=session.get('error'),
    )

@app.route('/position/reservate', methods=['POST'])
@auth
def reservate():
    position_id = request.form.get('position')
    vehicle_id = request.form.get('vehicle')
    vehicle = db.session.query(Vehicle).filter_by(id = vehicle_id).first()
    reservation_date = datetime.today() + timedelta(days=1)
    if vehicle.has_reservation():
        session['error'] = "Your vehicle has already reserved a position."
        return redirect(url_for('parking_page'))
    else:
        db.session.add(
            Reservation(
                position_id=position_id,
                vehicle_id=vehicle_id,
                date=reservation_date
            )
        )
        db.session.commit()
        return redirect(url_for('parking_page'))