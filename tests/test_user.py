import pytest
from finances.domain.user import User
import uuid

# user email tests
def test_user_has_email():
    fake_uuid = uuid.uuid4()

    user = User(email="test@email.com",
                password_hash= "test_hash",
                id=fake_uuid
                )
    assert user.email == "test@email.com"

def test_user_cannot_have_empty_email():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="",
            password_hash= "test_hash",
            id=fake_uuid
            )

def test_user_cannot_have_email_with_spaces():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="      ",
            password_hash= "test_hash",
            id=fake_uuid
            )

def test_user_email_cannot_be_int():
    fake_uuid = uuid.uuid4()

    with pytest.raises(TypeError):
        User(
            email=123,
            password_hash= "test_hash",
            id=fake_uuid
            )

def test_user_email_has_to_have_at_sign():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="teste-email",
            password_hash="test_hash",
            id=fake_uuid
            )

def test_user_email_has_text_before_at_sign():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="@test.com",
            password_hash="test_hash",
            id=fake_uuid
            )

def test_user_email_has_text_after_at_sign():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="test@",
            password_hash="test_hash",
            id=fake_uuid
            )

def test_user_email_cannot_have_two_at_sign():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="test@@email.com",
            password_hash="test_hash",
            id=fake_uuid
            )

def test_user_email_has_to_have_dot_at_end():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="test@email",
            password_hash="test_hash",
            id=fake_uuid
            )

def test_user_email_has_to_have_text_after_dot():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="test@email.",
            password_hash="test_hash",
            id=fake_uuid
            )

def test_user_email_extension_must_have_at_least_two_characters():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="test@email.b",
            password_hash="test_hash",
            id=fake_uuid
            )

# user password_hash tests
def test_user_has_password_hash():
    fake_uuid = uuid.uuid4()

    user = User(email="test@email.com",
                password_hash= "test_hash",
                id=fake_uuid
                )
    assert user.password_hash == "test_hash"

def test_user_cannot_have_empty_password_hash():
    fake_uuid = uuid.uuid4()

    with pytest.raises(ValueError):
        User(
            email="test@email.com",
            password_hash= "",
            id=fake_uuid
            )
        
def test_user_password_hash_must_be_string():
    fake_uuid = uuid.uuid4()

    with pytest.raises(TypeError):
        User(
            email="test@email.com",
            password_hash=123,
            id=fake_uuid
            )

# user id tests
def test_user_has_id():
    fake_uuid = uuid.uuid4()

    user = User(email="test@email.com",
            password_hash= "test_hash",
            id=fake_uuid
            )
    assert user.id == fake_uuid

def test_user_rejects_non_uuid_id():
    with pytest.raises(TypeError):
        User(email="test@email.com",
                password_hash= "test_hash",
                id="test_user_id_fake"
                )