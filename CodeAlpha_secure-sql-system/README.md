This project implements a secure cloud-based system to protect user data against SQL injection attacks. It demonstrates double-layer security using encryption and controlled access mechanisms.

Key Features:
Secure storage of user credentials using AES-256 encryption.
Capability code mechanism for controlled server access.
SQL injection detection to prevent unauthorized queries.
Double-layer security:
Layer 1: Input validation and SQL injection detection
Layer 2: Parameterized queries + capability code verification
Lightweight system accessible via Flask web app and MySQL database (XAMPP).

Technologies Used
Python 3.x
Flask – lightweight web framework
MySQL – XAMPP for database
PyCryptoDome – AES encryption (pip install pycryptodome)
HTML/CSS – User interface