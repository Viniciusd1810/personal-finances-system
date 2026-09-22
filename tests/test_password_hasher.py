from finances.infrastructure.security.password_hasher import Argon2PasswordHasher

def test_password_hasher_returns_hash():
    test_password = "testpass"
    hasher = Argon2PasswordHasher()
    hashed_password = hasher.hash_password(test_password)
    assert hashed_password != test_password

def test_password_hasher_verifies_correct_password():
    test_password = "testpass"
    hasher = Argon2PasswordHasher()
    hashed_password = hasher.hash_password(test_password)
    result = hasher.verify_password(hashed_password, test_password)
    assert result is True

def test_incorrect_password_returns_false():
    test_password = "testpass"
    hasher = Argon2PasswordHasher()
    hashed_password = hasher.hash_password(test_password)
    result = hasher.verify_password(hashed_password, "incorrect_password")
    assert result is False