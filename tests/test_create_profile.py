import uuid

from finances.application.create_profile import CreateProfile
from finances.domain.profile import Profile
from finances.domain.currency import Currency

def test_create_profile_returns_profile():
    user_id = uuid.uuid4()

    create_profile = CreateProfile()
    new_profile = create_profile.execute("test",
                    Currency.BRL,
                    user_id)
    assert isinstance(new_profile, Profile)

def test_create_profile_generates_different_ids_for_each_execution():
    user_id = uuid.uuid4()
    create_profile = CreateProfile()

    new_profile_1 = create_profile.execute("test",
                        Currency.BRL,
                        user_id)

    new_profile_2 = create_profile.execute("test",
                            Currency.BRL,
                            user_id)
    
    assert new_profile_1.id != new_profile_2.id