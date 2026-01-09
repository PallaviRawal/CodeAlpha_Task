def detect_sql_injection(text):
    blacklist = ["'", "--", ";", "/*", "*/", " OR ", " AND "]
    for pattern in blacklist:
        if pattern.lower() in text.lower():
            return True
    return False
