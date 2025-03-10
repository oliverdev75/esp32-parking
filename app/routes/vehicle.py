from flask import session, redirect, render_template, url_for
from app import app, db
from app.models.User import User
from app.models.Vehicle import Vehicle
from app.forms.VehicleForm import VehicleForm

@app.route('/vehicles')
def vehicles():
    if 'user' not in session:
        return redirect(url_for('login'))
    user = db.session.query(User).filter_by(id = session['user']).first()

    return render_template('vehicles.html',
        error=session.get('error'),
        user=user,
    )

@app.route('/vehicles/create', methods=['POST'])
def vehicle_create():
    if 'user' not in session:
        return redirect(url_for('login'))
    form = VehicleForm()
    if form.validate_on_submit():
        name = form.name.data
        plate_number = form.plate_number.data
        plate_check = db.session.query(Vehicle).filter_by(plate_number = plate_number).first()
        if plate_check:
            session['error'] = "Plate number already exists."
            return redirect(url_for('vehicles'))