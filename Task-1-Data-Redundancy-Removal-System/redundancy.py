import hashlib

def generate_hash(data):
    combined = f"{data['name']}{data['email']}{data['phone']}"
    return hashlib.sha256(combined.encode()).hexdigest()

def is_redundant(cursor, data_hash):
    query = "SELECT id FROM data_records WHERE data_hash=%s"
    cursor.execute(query, (data_hash,))
    return cursor.fetchone() is not None
