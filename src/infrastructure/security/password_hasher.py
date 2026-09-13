from argon2 import PasswordHasher

def hash_password(user_password):
    ph = PasswordHasher()
    hashed_password = ph.hash(user_password)
    return hashed_password