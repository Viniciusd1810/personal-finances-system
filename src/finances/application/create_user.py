from domain.user import User
from infrastructure.security import password_hasher

class CreateUser:
    def execute(self, email, user_password):
        password_hash = password_hasher.hash_password(user_password)

        new_user = User(email,password_hash)
        return new_user