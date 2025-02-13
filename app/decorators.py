from flask import session, redirect, url_for


def logged(func):
    def inner():
        if 'user' in session:
            return func()
        return redirect(url_for('login'))
    return inner

@logged
def is_admin(func):
    def inner():
        if session['user']['role'] == 'admin':
            return func()
        return redirect('/')
    return inner