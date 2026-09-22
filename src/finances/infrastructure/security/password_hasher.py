from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

class Argon2PasswordHasher:
    def __init__(self):
        self._ph = PasswordHasher()

    def hash_password(self, user_password):
        hashed_password = self._ph.hash(user_password)
        return hashed_password

    def verify_password(self, hashed_password, user_password):
        try:
            verification = self._ph.verify(hashed_password, user_password)
            return verification
        except VerifyMismatchError:
            return False