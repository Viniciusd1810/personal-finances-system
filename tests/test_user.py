import pytest
from domain.user import User

# user email tests
def test_user_has_email():
    user = User(email="test@email.com",
                password_hash= "test_hash"
                )
    assert user.email == "test@email.com"

def test_user_cannot_have_empty_email():
    with pytest.raises(ValueError):
        User(email="",
            password_hash= "test_hash"
            )

def test_user_cannot_have_email_with_spaces():
    with pytest.raises(ValueError):
        User(email="      ",
            password_hash= "test_hash"
            )

def test_user_email_cannot_be_int():
    with pytest.raises(TypeError):
        User(email=123,
            password_hash= "test_hash"
            )

# user password_hash tests
def test_user_has_password_hash():
    user = User(email="test@email.com",
                password_hash= "test_hash"
                )
    assert user._password_hash == "test_hash"

def test_user_cannot_have_empty_password_hash():
    with pytest.raises(ValueError):
        User(email="test@email.com",
            password_hash= ""
            )
        
def test_user_password_hash_cannot_be_int():
    with pytest.raises(TypeError):
        User(email="test@email.com",
            password_hash=123
            )
