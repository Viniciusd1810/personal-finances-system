import uuid
import pytest

from finances.application.create_profile import CreateProfile
from finances.domain.profile import Profile
from finances.domain.currency import Currency
from finances.domain.user import User
from fakes.fake_user_repository import FakeUserRepository

fake_user = User(email="test@email.com",
                password_hash="fake_hash",
                id=uuid.uuid4()
                )

def test_create_profile_returns_profile():
    fake_repository = FakeUserRepository()
    fake_repository.add(fake_user)
    create_profile = CreateProfile(fake_repository)

    new_profile = create_profile.execute(
        "test",
        Currency.BRL,
        fake_user.id)
    
    assert isinstance(new_profile, Profile)

def test_create_profile_generates_different_ids_for_each_execution():
    fake_repository = FakeUserRepository()
    fake_repository.add(fake_user)
    create_profile = CreateProfile(fake_repository)

    new_profile_1 = create_profile.execute(
        "test",
        Currency.BRL,
        fake_user.id)

    new_profile_2 = create_profile.execute(
        "test",
        Currency.BRL,
        fake_user.id
        )
    
    assert new_profile_1.id != new_profile_2.id

def test_create_profile_raises_error_when_user_does_not_exist():
    fake_repository = FakeUserRepository()
    create_profile = CreateProfile(fake_repository)

    noexistent_user_id = uuid.uuid4()

    with pytest.raises(ValueError):
        create_profile.execute(
        "test",
        Currency.BRL,
        noexistent_user_id
        )