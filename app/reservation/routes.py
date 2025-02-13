from .. import app
from .. import db
from ..models.User import User
from flask import render_template, redirect, url_for, session
from ..forms.LoginForm import LoginForm
import bcrypt


@app.route('/floor/<floor>', methods=['GET', 'POST'])
def floor1(floor):
    if floor > 0 and floor < 3:
        return render_template(f"parking-{floor}.html")
