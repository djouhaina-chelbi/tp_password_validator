def test_password_two_numbers():
    result = password("Abcdefgh")
    assert result["is_valid"] == False
    assert "The password must contain at least 2 numbers" in result["errors"]

