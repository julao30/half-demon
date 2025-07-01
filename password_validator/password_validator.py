import re

SPECIAL_CHARS = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]"

def is_valid_password(password):
    if len(password) < 8:
        return False
    if " " in password:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(SPECIAL_CHARS, password):
        return False
    return True

def has_secure_suffix(password):
    return password.endswith("!") or password.endswith("@")
