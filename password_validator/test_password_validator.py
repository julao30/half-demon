from password_validator import is_valid_password

def test_valid_password():
    assert is_valid_password("Abcdef1!")

def test_too_short():
    assert not is_valid_password("A1!a")

def test_missing_uppercase():
    assert not is_valid_password("abcdef1!")

def test_missing_lowercase():
    assert not is_valid_password("ABCDEF1!")

def test_missing_digit():
    assert not is_valid_password("Abcdefg!")

def test_missing_special():
    assert not is_valid_password("Abcdefg1")

def test_contains_space():
    assert not is_valid_password("Abc def1!")
