import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      # XAMPP default
        database="redundancy_db",
        port=3306
    )
