import pytest
import uuid

from finances.domain.profile import Profile
from finances.domain.currency import Currency

def test_profile_has_name():
    fake_profile_id = uuid.uuid4()
    fake_user_id = uuid.uuid4()

    profile = Profile(name="profile_test",
                      currency=Currency.BRL,
                      profile_id=fake_profile_id,
                      user_id=fake_user_id
                      )
    assert profile.name == "profile_test"

def test_profile_name_cannot_contain_only_spaces():
    fake_profile_id = uuid.uuid4()
    fake_user_id = uuid.uuid4()

    with pytest.raises(ValueError):
        Profile(name="  ",
                currency=Currency.BRL,
                profile_id=fake_profile_id,
                user_id=fake_user_id
                )

def test_profile_cannot_have_empty_name():
    fake_profile_id = uuid.uuid4()
    fake_user_id = uuid.uuid4()
    
    with pytest.raises(ValueError):
        Profile(name="",
                currency=Currency.BRL,
                profile_id=fake_profile_id,
                user_id=fake_user_id
                )

def test_profile_normalizes_name_whitespace():
    fake_profile_id = uuid.uuid4()
    fake_user_id = uuid.uuid4()

    profile = Profile(name=" test profile  ",
                      currency=Currency.BRL,
                      profile_id=fake_profile_id,
                      user_id=fake_user_id
                      )
    assert profile.name == "test profile"

def test_profile_name_cannot_be_int():
    fake_profile_id = uuid.uuid4()
    fake_user_id = uuid.uuid4()

    with pytest.raises(TypeError):
        Profile(name=1234,
                currency=Currency.BRL,
                profile_id=fake_profile_id,
                user_id=fake_user_id
                )

def test_profile_currency_cannot_be_string():
    fake_profile_id = uuid.uuid4()
    fake_user_id = uuid.uuid4()

    with pytest.raises(TypeError):
        Profile(name="Test",
                currency="BRL",
                profile_id=fake_profile_id,
                user_id=fake_user_id
                )

def test_profile_stores_currency():
    fake_profile_id = uuid.uuid4()
    fake_user_id = uuid.uuid4()

    profile = Profile(name="profile_test",
                      currency=Currency.BRL,
                      profile_id=fake_profile_id,
                      user_id=fake_user_id
                      )
    assert profile.currency is Currency.BRL