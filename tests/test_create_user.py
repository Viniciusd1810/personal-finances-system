import pytest
import uuid

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
    fake_hasher = FakePasswordHasher()
    create = CreateUser(fake_hasher)
    result = create.execute(email="test@email.com",
                            user_password="pass_test"
                            )
    assert isinstance(result, User)

def test_create_user_password_cannot_be_blank():
    fake_hasher = FakePasswordHasher()
    with pytest.raises(ValueError):
        create = CreateUser(fake_hasher)
        create.execute(email="test@email.com",
                        user_password="")

def test_create_user_password_cannot_contain_only_spaces():
    fake_hasher = FakePasswordHasher()
    with pytest.raises(ValueError):
            create = CreateUser(fake_hasher)
            create.execute(email="test@email.com",
                        user_password="      ")

def test_create_user_password_cannot_contain_blank_spaces():
    fake_hasher = FakePasswordHasher()
    with pytest.raises(ValueError):
            create = CreateUser(fake_hasher)
            create.execute(email="test@email.com",
                        user_password="1234   8")

def test_create_user_password_cannot_have_less_than_8_characters():
    fake_hasher = FakePasswordHasher()
    with pytest.raises(ValueError):
            create = CreateUser(fake_hasher)
            create.execute(email="test@email.com",
                        user_password="1234567")

def test_create_user_password_must_be_string():
    fake_hasher = FakePasswordHasher()
    with pytest.raises(TypeError):
        create = CreateUser(fake_hasher)
        create.execute(email="test@email.com",
                        user_password=12345678)

def test_create_user_has_hash_password():
    fake_hasher = FakePasswordHasher()
    create = CreateUser(fake_hasher)
    user = create.execute(email="test@email.com",
                        user_password="test_hash")
    assert user.password_hash == "fake_hash"

def test_create_user_password_arrives_at_hash_password():
    fake_hasher = FakePasswordHasher()
    create = CreateUser(fake_hasher)
    create.execute(email="test@email.com",
                        user_password="test_hash")
    assert fake_hasher.received_password == "test_hash"

# user id tests
def test_new_user_has_id_uuid():
    fake_hasher = FakePasswordHasher()
    create = CreateUser(fake_hasher)
    new_user = create.execute(email="test@email.com",
                        user_password="test_hash")
    assert isinstance(new_user.id,uuid.UUID)

def test_create_user_generates_different_ids_for_each_execution():
    fake_hasher = FakePasswordHasher()
    create = CreateUser(fake_hasher)

    new_user_1 = create.execute(email="test@email.com",
                        user_password="test_hash")

    new_user_2 = create.execute(email="test@email.com",
                        user_password="test_hash")
    assert new_user_1.id != new_user_2.id