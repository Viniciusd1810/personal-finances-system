import re

class User:
    def __init__(self, email,password_hash):
        if not isinstance(email, str):
            raise TypeError("Email cannot be this type")
        if email.strip() == "":
            raise ValueError("Email cannot be blank")

        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        if not re.fullmatch(email_pattern, email):
            raise ValueError("Invalid Email")

        """before, sep, end = email.partition("@") 
        if before == "":
            raise ValueError("Email has to have text before @")
        if sep != "@":
            raise ValueError("Email has to have @")
        if end == "":
            raise ValueError("Email has to have text after @")
        if "@" in end:
            raise ValueError("Email cannot have two @")
        if "." not in end:
            raise ValueError("Email has to have a dot")
        parts = end.split(".")
        if parts[1] == "":
            raise ValueError("email has to have a domain after dot")"""
        
        self.email: str = email

        if not isinstance(password_hash, str):
            raise TypeError("Password hash cannot be this type")
        if password_hash.strip() == "":
            raise ValueError("Password hash cannot be blank")
        self._password_hash = password_hash