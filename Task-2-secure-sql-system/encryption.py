from Crypto.Cipher import AES
import base64

KEY = b'12345678901234567890123456789012'  # 32 bytes = AES-256
IV  = b'1234567890123456'                  # 16 bytes

def encrypt_data(data):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    padded_data = data + (16 - len(data) % 16) * ' '
    encrypted = cipher.encrypt(padded_data.encode())
    return base64.b64encode(encrypted).decode()
