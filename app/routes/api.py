from flask import jsonify, request, session
from datetime import datetime
from app import app, db
from app.models.Vehicle import Vehicle
from app.models.Position import Position
from app.models.Log import Log
from app.models.Reservation import Reservation

@app.route('/api/checkplate')
def checkplate():
    plate = request.args.get('plate')
    if not plate:
        return jsonify({
            'status': 'error',
            'message': 'no plate specified',
        })
    vehicle = db.session.query(Vehicle).filter_by(plate_number = plate).first()
    if not vehicle:
        return jsonify({
            'status': 'error',
            'message': 'vehicle not found',
        })
    db.session.add(Log(vehicle_id=vehicle.id))
    db.session.commit()
    return jsonify({
        'status': 'ok',
        'user': vehicle.user,
    })

@app.route('/api/vehicleexit', methods=['POST'])
def vehicleexit():
    plate = request.args.get('plate')
    if not plate:
        return jsonify({
            'status': 'error',
            'message': 'no plate specified',
        })
    vehicle = db.session.query(Vehicle).filter_by(plate_number=plate).first()
    if not vehicle:
        return jsonify({
            'status': 'error',
            'message': 'vehicle not found',
        })
    for log in vehicle.logs:
        if datetime.strptime(log.entry_date, "%d/%m/%Y").date == datetime.strptime(datetime.today()):
            log.exit_date = datetime.now()
            break
    return jsonify({
        'status': 'ok',
        'user': vehicle.user
    })

def change_position_status(position_id, status):
    position = db.session.query(Position).filter_by(code=position_id).first()
    if not position:
        return jsonify({
            'status': 'error',
            'message': 'position not found',
        })
    position.busy = status
    db.session.commit()
    return jsonify({
        'status': 'ok',
        'position_status': db.session.query(Position).filter_by(code=position_id).first().busy
    })

@app.route('/api/position/empty', methods=['POST'])
def empty_position():
    position_id = request.get_json(force=True).get('position')
    if not position_id:
        return jsonify({
            'status': 'error',
            'message': 'no position specified',
        })
    return change_position_status(position_id, False)

@app.route('/api/position/busy', methods=['POST'])
def busy_position():
    position_id = request.get_json(force=True).get('position')
    if not position_id:
        return jsonify({
            'status': 'error',
            'message': 'no position specified',
        })
    return change_position_status(position_id, True)

@app.route('/api/positions')
def positionsa():
    position = db.session.query(Reservation).filter_by(vehicle_id=request.args.get('vehicle')).first()
    return jsonify({
        'status': 'ok',
        'reservations': position.to_dict(),
    })