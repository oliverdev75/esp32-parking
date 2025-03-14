from flask import session, redirect, url_for

def auth(f):
    def decorator():
        if 'user' not in session:
            return redirect(url_for('login'))
        return f()
    decorator.__name__ = f.__name__
    return decorator

def guest(f):
    def decorator():
        if 'user' in session:
            return redirect(url_for('index'))
        return f()
    decorator.__name__ = f.__name__
    return decorator
