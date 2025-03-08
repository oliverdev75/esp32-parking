from app import app
from app import db
from app.models.Position import Position
from flask import render_template, redirect, url_for, session, request


@app.route('/parking', methods=['GET', 'POST'])
def parkingPage():
    if 'user' not in session:
        return redirect(url_for('login'))
    position_id = request.args.get('position')
    specified_position = None
    if position_id:
        specified_position = db.session.query(Position).filter_by(code = position_id).first()
    positions = db.session.query(Position).all()
    return render_template('parking.html',
       specified_position=specified_position,
       positions=positions,
       user=session['user'],
    )

@app.route('/position/reservate', methods=['POST'])
def reservate():
    if 'user' not in session:
        return redirect(url_for('login'))
