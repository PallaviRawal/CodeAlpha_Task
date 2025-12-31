def validate_data(data):
    if not data.get("name"):
        return False
    if not data.get("email") or "@" not in data["email"]:
        return False
    if not data.get("phone") or len(data["phone"]) != 10:
        return False
    return True
