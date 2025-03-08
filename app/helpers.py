import bcrypt

def encrypt(password: str):
    bcrypt.hashpw(password.encode(), bcrypt.gensalt())