import requests
import base64
import tkinter as tk
from tkinter import messagebox


# Funktion zum Herunterladen einer Datei von GitHub
def download_file_from_github(repo_owner, repo_name, file_path, branch='main'):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}?ref={branch}'
    response = requests.get(url)
    if response.status_code == 200:
        file_info = response.json()
        file_content = file_info.get('content')
        encoding = file_info.get('encoding')

        if encoding == 'base64':
            file_content = base64.b64decode(file_content)

        mode = 'wb' if file_info.get('type') == 'file' else 'w'
        with open(file_path, mode) as file:
            file.write(file_content)
        return True
    else:
        print('Fehler beim Herunterladen der Datei:', response.status_code, response.text)
        return False


def show_download_message(missing_files, repo_owner, repo_name):
    def download_files():
        success = True
        for file in missing_files:
            if not download_file_from_github(repo_owner, repo_name, file):
                success = False
        if success:
            messagebox.showinfo("Download", "All files downloaded successfully.")
        else:
            messagebox.showerror("Download Error", "Some files could not be downloaded.")
        download_window.destroy()

    root = tk.Tk()
    root.withdraw()  # Hauptfenster ausblenden

    download_window = tk.Toplevel(root)
    download_window.title("Missing Files")
    tk.Label(download_window, text=f"Required files not found: {', '.join(missing_files)}").pack(pady=10)
    tk.Button(download_window, text="Download Files", command=download_files).pack(pady=5)
    tk.Button(download_window, text="Cancel", command=download_window.destroy).pack(pady=5)

    root.mainloop()


# Beispielaufruf (kann entfernt werden, wenn nicht benötigt)
if __name__ == '__main__':
    missing_files = ["password_display.py", "password_manager.py", "password_generator.py"]
    show_download_message(missing_files, 'LEcombi', 'Password-Manager')