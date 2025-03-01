from cryptography.fernet import Fernet
import subprocess

# Generate encryption key (store this key securely)
key = Fernet.generate_key()
with open('../key.key', 'wb') as keyfile:
    keyfile.write(key)

print(f"Encryption Key: {key.decode()}")

#Paste the Generated Data in the Root folder
subprocess.run(["python", "run2.py"], cwd="../Root_password_Generator")