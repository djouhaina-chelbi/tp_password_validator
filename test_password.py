def test_password_special_character():
    result = password("Abcd1234")
    assert result["is_valid"] == False
    assert "Password must contain at least one special character" in result["errors"]

