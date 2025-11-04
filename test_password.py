def test_password_capital_letter():
    result = password("abcd@123")
    assert result["is_valid"] == False
    assert "Password must contain at least one capital letter" in result["errors"]
