from db import get_connection
from pricing import calculate_price
from ticket import generate_pass_hash

def book_bus_pass(user_id, route):
    try:
        price = calculate_price(route)
    except ValueError as e:
        print("Booking failed:", e)
        return

    conn = get_connection()
    cursor = conn.cursor()

    pass_hash = generate_pass_hash(user_id, route)

    query = """
    INSERT INTO bus_pass (user_id, route, price, pass_hash)
    VALUES (%s, %s, %s, %s)
    """

    try:
        cursor.execute(query, (user_id, route, price, pass_hash))
        conn.commit()
        print("Bus pass booked successfully")
    except Exception:
        print("Duplicate booking detected")
    finally:
        cursor.close()
        conn.close()
 
routes = [
    "Station A - Station B",
    "Station A - Station C",
    "Station B - Station C"
]

for route in routes:
    book_bus_pass(1, route)


