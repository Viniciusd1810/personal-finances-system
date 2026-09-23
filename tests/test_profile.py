import pytest
from finances.domain.profile import Profile
from finances.domain.currency import Currency

def test_profile_has_name():
    profile = Profile(name="profile_test",currency=Currency.BRL)
    assert profile.name == "profile_test"

def test_profile_cannot_have_empty_name():
    with pytest.raises(ValueError):
        Profile(name="",currency=Currency.BRL)

def test_profile_normalizes_name_whitespace():
        profile = Profile(name=" test profile  ",currency=Currency.BRL)
        assert profile.name == "test profile"

def test_profile_name_cannot_be_int():
    with pytest.raises(TypeError):
        Profile(name=1234,currency=Currency.BRL)

def test_profile_currency_cannot_be_string():
    with pytest.raises(TypeError):
        Profile(name="Test",currency="BRL")

def test_profile_stores_currency():
    profile = Profile(name="profile_test",currency=Currency.BRL)
    assert profile.currency is Currency.BRL