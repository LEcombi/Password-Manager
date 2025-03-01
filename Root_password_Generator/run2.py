from cryptography.fernet import Fernet
import configparser

# Load encryption key from file
with open('../key.key', 'rb') as keyfile:
    key = keyfile.read()
cipher_suite = Fernet(key)

# Set root password (replace with your own secure password)

root_password = "my_secure_root_password"

encrypted_password = cipher_suite.encrypt(root_password.encode())

# Save encrypted password to config file
config = configparser.ConfigParser()
config['credentials'] = {'root_password': encrypted_password.decode()}
with open('../config.cfg', 'w') as configfile:
    config.write(configfile)

print("Encrypted root password saved to config.cfg")
#Paste the Generated Data in the Root folder