import tkinter as tk
from tkinter import messagebox
from translate_text import load_config, translate_text

# Load the target language from the config file
target_language = load_config()

def copy_to_clipboard(root, password):
    """Function to copy the password to the clipboard"""
    root.clipboard_clear()
    root.clipboard_append(password)
    copied_message = translate_text("Password copied to clipboard.", target_language)
    messagebox.showinfo("Copied", copied_message)

def show_all_passwords(root, entries, reload_callback, delete_callback):
    """Function to display all passwords in the database"""
    def reload_passwords():
        output_window.destroy()
        reload_callback()

    output_window = tk.Toplevel(root)
    output_window.title(translate_text("All Passwords", target_language))
    output_window.geometry("400x450")
    output_window.configure(bg="#2E2E2E")
    output_window.iconbitmap("key.ico")

    label_font = ("Arial", 12, "bold")
    button_font = ("Arial", 10)
    password_font = ("Arial", 14, "bold")

    for service, password in entries:
        frame = tk.Frame(output_window, bg="#2E2E2E")
        frame.pack(fill=tk.X, pady=5)

        password_label = tk.Label(frame, text=f"{service}: {password}", font=password_font, bg="#2E2E2E", fg="#FFFFFF", justify=tk.LEFT)
        password_label.pack(side=tk.LEFT, padx=10)

        copy_button_text = translate_text("Copy", target_language)
        copy_button = tk.Button(frame, text=copy_button_text, font=button_font, command=lambda p=password: copy_to_clipboard(root, p), bg="#2196F3", fg="white")
        copy_button.pack(side=tk.RIGHT, padx=10)

        delete_button_text = translate_text("Delete", target_language)
        delete_button = tk.Button(frame, text=delete_button_text, font=button_font, command=lambda s=service: delete_callback(s, output_window), bg="#FF0000", fg="white")
        delete_button.pack(side=tk.RIGHT, padx=10)

    reload_button_text = translate_text("Reload Passwords", target_language)
    reload_button = tk.Button(output_window, text=reload_button_text, font=button_font, command=reload_passwords, bg="#FF5722", fg="white")
    reload_button.pack(pady=10)