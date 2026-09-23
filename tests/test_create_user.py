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
    fakeHash = FakePasswordHasher()
    create = CreateUser(fakeHash)
    result = create.execute(email="test@email.com",
                            user_password="pass_test"
                            )
    assert isinstance(result, User)

def test_create_user_password_cannot_be_blank():
    fakeHash = FakePasswordHasher()
    with pytest.raises(ValueError):
        create = CreateUser(fakeHash)
        create.execute(email="test@email.com",
                        user_password="")

def test_create_user_password_cannot_contain_only_spaces():
    fakeHash = FakePasswordHasher()
    with pytest.raises(ValueError):
            create = CreateUser(fakeHash)
            create.execute(email="test@email.com",
                            user_password="      ")

def test_create_user_password_cannot_contains_blank_spaces():
    fakeHash = FakePasswordHasher()
    with pytest.raises(ValueError):
            create = CreateUser(fakeHash)
            create.execute(email="test@email.com",
                            user_password="1234   8")

def test_create_user_password_cannot_have_less_than_8_characters():
    fakeHash = FakePasswordHasher()
    with pytest.raises(ValueError):
            create = CreateUser(fakeHash)
            create.execute(email="test@email.com",
                            user_password="1234567")

def test_create_user_password_must_be_string():
    fakeHash = FakePasswordHasher()
    with pytest.raises(TypeError):
        create = CreateUser(fakeHash)
        create.execute(email="test@email.com",
                        user_password=12345678)

def test_create_user_hash_password_works():
    fakeHash = FakePasswordHasher()
    create = CreateUser(fakeHash)
    user = create.execute(email="test@email.com",
                    user_password="test_hash")
    assert user.password_hash == "fake_hash"

def test_create_user_password_arrives_at_hash_password():
    fakeHash = FakePasswordHasher()
    create = CreateUser(fakeHash)
    create.execute(email="test@email.com",
                    user_password="test_hash")
    assert fakeHash.received_password == "test_hash"