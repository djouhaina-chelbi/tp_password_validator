def test_password_too_short():
    result = password("abc")
    assert result["is_valid"] == False
    assert "Password must be at least 8 characters" in result["errors"]
