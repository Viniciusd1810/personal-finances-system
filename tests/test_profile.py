import pytest
from finances.domain.profile import Profile

def test_profile_has_name():
    profile = Profile(profile_name="profile_test",currency="BRL")
    assert profile._profile_name == "profile_test"

def test_profile_cannot_have_empty_name():
    with pytest.raises(ValueError):
        Profile(profile_name="",currency="BRL")

def test_profile_name_cannot_be_int():
    with pytest.raises(TypeError):
        Profile(profile_name=1234,currency="BRL")