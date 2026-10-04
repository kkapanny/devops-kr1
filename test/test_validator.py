# tests/test_validator.py
import validator
def test_validate_email():
    assert validator.validate_email("test@example.com") == True
    assert validator.validate_email("invalid") == False

def test_validate_phone():
    assert validator.validate_phone("+79991234567") == True
    assert validator.validate_phone("89991234567") == False
    assert validator.validate_phone("+7999123") == False