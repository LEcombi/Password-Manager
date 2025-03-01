import sqlite3
from cryptography.fernet import Fernet
import configparser

# Load encryption key from file
with open('key.key', 'rb') as keyfile:
    key = keyfile.read()
cipher_suite = Fernet(key)

# Load encrypted root password from config file
config = configparser.ConfigParser()
config.read('config.cfg')
encrypted_password = config['credentials']['root_password']
root_password = cipher_suite.decrypt(encrypted_password.encode()).decode()

# Database setup
conn = sqlite3.connect('passwords.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS passwords
             (service text, encrypted_password text)''')
conn.commit()

# Function to save a password for a specific service
def save_password(service, password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    c.execute("INSERT INTO passwords VALUES (?, ?)", (service, encrypted_password))
    conn.commit()

# Function to retrieve a password for a specific service
def retrieve_password(service):
    c.execute("SELECT encrypted_password FROM passwords WHERE service=?", (service,))
    result = c.fetchone()
    if result:
        encrypted_password = result[0]
        password = cipher_suite.decrypt(encrypted_password).decode()
        return password
    else:
        return None

# Function to unlock the database using the root password
def unlock_database(input_password):
    if input_password == root_password:
        c.execute("SELECT service, encrypted_password FROM passwords")
        entries = c.fetchall()
        decrypted_entries = [(service, cipher_suite.decrypt(encrypted_password).decode()) for service, encrypted_password in entries]
        return decrypted_entries
    else:
        return None

# Function to get all passwords from the database
def get_all_passwords():
    c.execute("SELECT service, encrypted_password FROM passwords")
    entries = c.fetchall()
    decrypted_entries = [(service, cipher_suite.decrypt(encrypted_password).decode()) for service, encrypted_password in entries]
    return decrypted_entries

# Function to delete a password for a specific service
def delete_password(service):
    c.execute("DELETE FROM passwords WHERE service=?", (service,))
    conn.commit()

# Function to close the database connection
def close_connection():
    conn.close()