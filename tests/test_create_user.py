import pytest
from finances.application.create_user import CreateUser
from finances.domain.user import User

# Fake password hasher to test dependency injection

class FakePasswordHasher():
    def __init__(self):
        self.received_password = None
    def hash_password(self, test_password):
        self.received_password = test_password
        return "fake_hash"
    
def test_create_user_returns_user():
    FakeHash = FakePasswordHasher()

    create = CreateUser(FakeHash)

    result = create.execute(email="test@email.com",
                            user_password="pass_test"
                            )
    assert isinstance(result, User)

def test_create_user_password_cannot_be_blank():
    FakeHash = FakePasswordHasher()
    with pytest.raises(ValueError):
        create = CreateUser(FakeHash)
        create.execute(email="test@email.com",
                        user_password="")

def test_create_user_password_cannot_contain_only_spaces():
    FakeHash = FakePasswordHasher()
    with pytest.raises(ValueError):
            create = CreateUser(FakeHash)
            create.execute(email="test@email.com",
                            user_password="      ")

def test_create_user_password_cannot_contains_blank_spaces():
    FakeHash = FakePasswordHasher()
    with pytest.raises(ValueError):
            create = CreateUser(FakeHash)
            create.execute(email="test@email.com",
                            user_password="1234   8")

def test_create_user_password_cannot_have_less_than_8_characters():
    FakeHash = FakePasswordHasher()
    with pytest.raises(ValueError):
            create = CreateUser(FakeHash)
            create.execute(email="test@email.com",
                            user_password="1234567")

def test_create_user_password_must_be_string():
    FakeHash = FakePasswordHasher()
    with pytest.raises(TypeError):
        create = CreateUser(FakeHash)
        create.execute(email="test@email.com",
                        user_password=12345678)

def test_create_user_hash_password_works():
    FakeHash = FakePasswordHasher()
    create = CreateUser(FakeHash)
    user = create.execute(email="test@email.com",
                    user_password="test_hash")
    assert user._password_hash == "fake_hash"

def test_create_user_password_arrives_at_hash_password():
    FakeHash = FakePasswordHasher()
    create = CreateUser(FakeHash)
    create.execute(email="test@email.com",
                    user_password="test_hash")
    assert FakeHash.received_password == "test_hash"