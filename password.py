def password(password: str):
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")
    numbers = re.findall(r"[0-9]", password)
    if len(numbers) < 2:
        errors.append("The password must contain at least 2 numbers")
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }
