from password_validator import has_secure_suffix

def test_password_with_secure_suffix():
    assert has_secure_suffix("HelloWorld!") is True

def test_password_with_other_suffix():
    assert has_secure_suffix("HelloWorld123") is False
