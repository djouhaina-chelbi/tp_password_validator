def test_password_valid():
    result = password("Abcd@123")
    assert result["is_valid"] == True
    assert result["errors"] == []
