from flask import jsonify, request
from sqlalchemy.orm.unitofwork import PostSortRec

from app import app, db
from app.models.Vehicle import Vehicle
from app.models.Position import Position
from app.models.User import User

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

    return jsonify({
        'status': 'ok',
        'user': vehicle.user,
    })

def change_position_status(id, status):
    position = db.session.query(Position).filter_by(code=id).first()
    if not position:
        return jsonify({
            'status': 'error',
            'message': 'position not found',
        })
    position.busy = status
    db.session.commit()
    return jsonify({
        'status': 'ok',
        'position_status': db.session.query(Position).filter_by(code=id).first().busy
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
    positions = Position.query.all()

    return jsonify({
        'status': 'ok',
        'reservations': [position.is_reserved() for position in positions],
    })