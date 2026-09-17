from finances.domain.user import User

class CreateUser:
    def __init__(self, password_hasher):
        self._password_hasher = password_hasher

    def execute(self, email, user_password):
        if not isinstance(user_password,str):
            raise TypeError("User password must be a string")
        if user_password.strip() == "":
            raise ValueError("User password cannot be blank")
        if " " in user_password:
            raise ValueError("User password cannot have blank spaces")
        if len(user_password) < 8:
            raise ValueError("User password cannot have less than 8 characters")
        
        password_hash = self._password_hasher.hash_password(user_password)
        new_user = User(email,password_hash)
        return new_user