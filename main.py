import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import password_generator
import password_manager
import password_display  # Import the password_display module

# Function to generate and display a password
def show_password():
    try:
        length = int(entry.get())
        password = password_generator.generate_password(length)
        password_label.config(text=password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_label.cget("text"))
    messagebox.showinfo("Copied", "Password copied to clipboard.")

# Function to save the generated password for a specific service
def save_password():
    service = simpledialog.askstring("Input", "Enter the service name:")
    password = password_label.cget("text")
    if service and password:
        password_manager.save_password(service, password)
        messagebox.showinfo("Saved", "Password saved successfully.")
    else:
        messagebox.showerror("Error", "Service name or password is missing.")

# Function to copy a specific password to the clipboard
def copy_to_clipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard.")

# Function to unlock the database using the root password
def unlock_database():
    root_pass = simpledialog.askstring("Input", "Enter root password:", show='*')
    if root_pass:
        entries = password_manager.unlock_database(root_pass)
        if entries:
            show_passwords_window(entries)
            enable_password_entry()
        else:
            messagebox.showerror("Error", "Invalid root password or no entries found.")
    else:
        messagebox.showerror("Error", "Root password is missing.")

# Function to enable password entry after unlocking the database
def enable_password_entry():
    add_password_button.config(state=tk.NORMAL)

# Function to add a new password to the database
def add_password():
    service = simpledialog.askstring("Input", "Enter the service name:")
    password = simpledialog.askstring("Input", "Enter the password:")
    if service and password:
        password_manager.save_password(service, password)
        messagebox.showinfo("Saved", "Password saved successfully.")
    else:
        messagebox.showerror("Error", "Service name or password is missing.")

# Function to show passwords window
def show_passwords_window(entries):
    password_display.show_all_passwords(root, entries, reload_passwords, delete_password)

# Function to reload passwords from the database
def reload_passwords():
    entries = password_manager.get_all_passwords()
    if entries:
        show_passwords_window(entries)
    else:
        messagebox.showerror("Error", "No entries found.")

# Function to delete a password
def delete_password(service, window):
    password_manager.delete_password(service)
    window.destroy()
    reload_passwords()

# Function to handle entry click event
def on_entry_click(event):
    """Function that is executed when the entry field is clicked"""
    if entry.get() == '12':
        entry.delete(0, "end")  # Removes the placeholder text
        entry.config(fg='white')

# Function to handle entry focusout event
def on_focusout(event):
    """Function that is executed when the entry field loses focus"""
    if entry.get() == '':
        entry.insert(0, '12')
        entry.config(fg='grey')

# Create the main window
root = tk.Tk()
root.title("Password Generator and Manager")
root.iconbitmap("key.ico")
root.geometry("400x450")

# Dark Mode Style
root.configure(bg="#2E2E2E")
label_font = ("Arial", 12, "bold")
button_font = ("Arial", 10)
password_font = ("Arial", 14, "bold")

# Create and place the widgets
label = tk.Label(root, text="Enter the desired password length:", font=label_font, bg="#2E2E2E", fg="#FFFFFF")
label.pack(pady=10)

entry = tk.Entry(root, font=label_font, bg="#555555", fg="#FFFFFF", insertbackground="#FFFFFF")
entry.insert(0, '12')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#2E2E2E")
button_frame.pack(pady=10)

generate_button = tk.Button(button_frame, text="Generate Password", font=button_font, command=show_password, bg="#4CAF50", fg="white")
generate_button.grid(row=0, column=0, padx=10)

copy_button = tk.Button(button_frame, text="Copy Password", font=button_font, command=copy_to_clipboard, bg="#2196F3", fg="white")
copy_button.grid(row=0, column=1, padx=10)

password_label = tk.Label(root, text="", font=password_font, bg="#2E2E2E", fg="#FFFFFF")
password_label.pack(pady=20)

save_button = tk.Button(root, text="Save Password", font=button_font, command=save_password, bg="#FF5722", fg="white")
save_button.pack(pady=10)

unlock_button = tk.Button(root, text="Unlock Database", font=button_font, command=unlock_database, bg="#9C27B0", fg="white")
unlock_button.pack(pady=10)

add_password_button = tk.Button(root, text="Add Password", font=button_font, command=add_password, bg="#FF5722", fg="white", state=tk.DISABLED)
add_password_button.pack(pady=10)

# Run the application
root.mainloop()

# Close the database connection when the application is closed
password_manager.close_connection()