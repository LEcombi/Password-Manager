import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import configparser

def generate_key_and_encrypt_password():
    # Generate encryption key (store this key securely)
    key = Fernet.generate_key()
    with open('../key.key', 'wb') as keyfile:
        keyfile.write(key)

    # Load encryption key from file
    with open('../key.key', 'rb') as keyfile:
        key = keyfile.read()
    cipher_suite = Fernet(key)

    # Set root password (replace with your own secure password)
    root_password = password_entry.get()
    if not root_password:
        messagebox.showerror("Error", "Please enter a root password.")
        return

    encrypted_password = cipher_suite.encrypt(root_password.encode())

    # Save encrypted password to config file
    config = configparser.ConfigParser()
    config['credentials'] = {'root_password': encrypted_password.decode()}
    with open('../config.cfg', 'w') as configfile:
        config.write(configfile)

    messagebox.showinfo("Success", "Encryption key and root password saved successfully." + "\n" + "You can close this window.")

# Create the main window
root = tk.Tk()
root.title("Setup Encryption Key and Root Password")

# Create and place the widgets
tk.Label(root, text="Enter Root Password:").pack(pady=10)
password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Key and Encrypt Password", command=generate_key_and_encrypt_password)
generate_button.pack(pady=20)

# Run the application
root.mainloop()