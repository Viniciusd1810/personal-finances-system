import pytest
from finances.domain.profile import Profile

def test_profile_has_name():
    profile = Profile(name="profile_test",currency="BRL")
    assert profile.name == "profile_test"

def test_profile_cannot_have_empty_name():
    with pytest.raises(ValueError):
        Profile(name="",currency="BRL")

def test_profile_name_cannot_be_int():
    with pytest.raises(TypeError):
        Profile(name=1234,currency="BRL")