import hashlib

def password_hash(pwd):
    salt = b'somesalt' # Adicione um sal para aumentar a segurança do hash
    password = hashlib.pbkdf2_hmac('sha256', pwd.encode('utf-8'), salt, 100000)
    return password.hex()

