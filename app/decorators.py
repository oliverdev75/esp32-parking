from flask import session, redirect, url_for
from . import app


# def logged(func):
#     with app.app_context():
#         if 'user' in session:
#             return func()
#         return redirect(url_for('login'))
#
# def guest(func):
#     with app.app_context():
#         if 'user' not in session:
#             return func()
#         return redirect(url_for('index'))
#
# @logged
# def is_admin(func):
#     def inner():
#         if session['user']['role'] == 'admin':
#             return func()
#         return redirect(url_for('index'))
#     return inner