import hashlib

def generate_pass_hash(user_id, route):
    raw_data = f"{user_id}-{route}"
    return hashlib.sha256(raw_data.encode()).hexdigest()
