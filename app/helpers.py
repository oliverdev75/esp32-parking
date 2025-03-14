import bcrypt

def encrypt(password: str):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())