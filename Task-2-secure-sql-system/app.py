from flask import Flask, render_template, request, redirect
from encryption import encrypt_data
from security import detect_sql_injection
import mysql.connector
import uuid


app = Flask(__name__)

# ---------------- HELPER FUNCTION ----------------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="secure_system1"  # Make sure DB exists!
    )

# ---------------- HOME ----------------
@app.route('/')
def home():
    return redirect('/login')

# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            message = "All fields are required."
            return render_template('register.html', message=message)

        # Security Layer 1: SQL Injection Detection
        if detect_sql_injection(username) or detect_sql_injection(password):
            message = "SQL Injection attempt detected! Registration blocked."
            return render_template('register.html', message=message)

        encrypted_password = encrypt_data(password)
        capability_code = str(uuid.uuid4())

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, capability_code) VALUES (%s, %s, %s)",
            (username, encrypted_password, capability_code)
        )
        conn.commit()
        conn.close()

        # Show capability code clearly
        message = f"""
        Registration Successful!<br><br>
        <strong>Your Capability Code:</strong><br>
        <span style='color:#155724'>{capability_code}</span><br><br>
        Please save this code. You will need it to login.
        """

    return render_template('register.html', message=message)


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        capability = request.form['capability']

        # Layer 1: SQL Injection detection
        if detect_sql_injection(username) or detect_sql_injection(password):
            error = "SQL Injection attempt detected! Access blocked."
            return render_template('login.html', error=error)

        # Encrypt password
        encrypted_password = encrypt_data(password)

        # Layer 2: Parameterized query
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT password, capability_code FROM users WHERE username=%s",
            (username,)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            db_password, db_capability = user
            if db_password == encrypted_password and db_capability == capability:
                return f"Login Successful! Capability Code Verified: {db_capability}"
        error = "Invalid username, password, or capability code."

    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)
