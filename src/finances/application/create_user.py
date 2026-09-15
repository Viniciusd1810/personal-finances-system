from finances.domain.user import User

class CreateUser:
    def __init__(self, password_hasher):
        self._password_hasher = password_hasher

    def execute(self, email, user_password):
        password_hash = self._password_hasher.hash_password(user_password)

        new_user = User(email,password_hash)
        return new_user