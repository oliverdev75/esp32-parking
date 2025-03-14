from flask import session, redirect, render_template, url_for, request
from app.decorators import auth
from app import app, db
from app.models.User import User
from app.models.Vehicle import Vehicle
from app.forms.VehicleForm import VehicleForm

@app.route('/vehicles')
def vehicles():
    if 'user' not in session:
        return redirect(url_for('login'))
    user = db.session.query(User).filter_by(id = session['user']).first()
    form = VehicleForm()
    error = None
    if session.get('error'):
        error = session.get('error')
        session.pop('error')
    return render_template('vehicles.html',
        error=error,
        user=user,
        form=form
    )

def check_plate(plate):
    vehicle = db.session.query(Vehicle).filter_by(plate_number=plate).first()
    if vehicle:
        session['error'] = "Plate number already exists."
        return False
    return True

@app.route('/vehicle/create', methods=['POST'])
@auth
def vehicle_create():
    if request.method == 'POST':
        plate = request.form['plate_number']
        if check_plate(plate):
            name = request.form['name']
            user = db.session.query(User).filter_by(id = session['user']).first()
            Vehicle(name=name, plate_number=plate, user=user)
            db.session.commit()
        else:
            session['error'] = "Plate number already exists."
        return redirect(url_for('vehicles'))
    return redirect(url_for('vehicles'))

@app.route('/vehicle/update', methods=['POST'])
@auth
def vehicle_update():
    if request.method == 'POST':
        name = request.form['name']
        plate = request.form['plate_number']
        vehicle_id = request.form['id']
        if not check_plate(plate):
            session['error'] = "Plate number already exists."
            return redirect(url_for('vehicles'))
        vehicle = db.query(Vehicle).filter_by(id = vehicle_id).first()
        if vehicle:
            vehicle.name = name
            vehicle.plate_number = plate
            db.session.commit()
            return redirect(url_for('vehicles'))
    return redirect(url_for('vehicles'))

@app.route('/vehicle/delete', methods=['POST'])
@auth
def vehicle_delete():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        vehicle_id = request.form['vehicle']
        vehicles = db.session.query(Vehicle).filter_by(user_id = session['user']).all()
        if len(vehicles) == 1:
            session['error'] = "You just have one vehicle, cannot delete it."
            return redirect(url_for('vehicles'))
        vehicle = db.session.query(Vehicle).filter_by(id = vehicle_id).first()
        for reservation in vehicle.reservations:
            db.session.delete(reservation)
        for log in vehicle.logs:
            db.session.delete(log)
        db.session.commit()
        if vehicle:
            db.session.delete(vehicle)
            db.session.commit()
            return redirect(url_for('vehicles'))