import pytest
from finances.application.create_user import CreateUser
from finances.domain.user import User

class FakePasswordHasher():
    def hash_password(self, test_password):
        return "fake_hash"

Fake_Hash = FakePasswordHasher()

def test_create_user_returns_user():
    create = CreateUser(Fake_Hash)

    result = create.execute(email="test@email.com",
                            user_password="pass_test"
                            )
    assert isinstance(result, User)