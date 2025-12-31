from db import get_connection
from validation import validate_data
from redundancy import generate_hash, is_redundant

def insert_data(data):
    conn = get_connection()
    cursor = conn.cursor()

    if not validate_data(data):
        print(" False Positive / Invalid Data")
        return

    data_hash = generate_hash(data)

    if is_redundant(cursor, data_hash):
        print("Redundant Data Detected")
        return

    query = """
    INSERT INTO data_records (name, email, phone, data_hash)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (
        data["name"],
        data["email"],
        data["phone"],
        data_hash
    ))
    conn.commit()
    print("Unique Data Inserted Successfully")

    cursor.close()
    conn.close()

# Test data
if __name__ == "__main__":
    data = {
        "name": "Sneha",
        "email": "Sneha@gmail.com",
        "phone": "1234567899"
    }
    insert_data(data)
