import requests
import tkinter as tk
import os

config_file_path = "apikey.config"
default_api_key = ""

def set_status(status, color="black"):
    status_dynamic_label.config(text=status, fg=color)

def download_mod_files():
    key_api = api_key_entry.get()
    mod_id = mod_id_entry.get()

    if not key_api or not mod_id:
        set_status("Validation Error: Fields cannot be empty", "red")
        return

    url_api = f'https://api.mod.io/v1/games/264/mods/{mod_id}/files'

    headers = {
        'Accept': 'application/json',
    }

    parameters = {
        'api_key': key_api,
    }

    response = requests.get(url_api, params=parameters, headers=headers)
    set_status("Status:")

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            url_download = data['data'][0]['download']['binary_url']
            download_mod_file(mod_id, url_download)
            mod_id_entry.delete(0, 'end')
        else:
            set_status("No mod files found", "red")
    else:
        set_status(f"Failed to download mod files. Status code: {response.status_code}", "red")

def download_mod_file(mod_id, url):
    response = requests.get(url)
    if response.status_code == 200:
        download_folder = "Downloaded Files"
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        filename = os.path.join(download_folder, f"{mod_id}.zip")
        with open(filename, 'wb') as file:
            file.write(response.content)
        set_status(f"File Downloaded -> {filename}", "green")
    else:
        set_status(f"Failed to download the file. Status code: {response.status_code}", "red")

def load_api_key_from_file():
    if os.path.exists(config_file_path):
        try:
            with open(config_file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if not line.startswith("#"):
                        api_key = line.strip()
                        api_key_entry.delete(0, 'end')
                        api_key_entry.insert(0, api_key)
                        break
        except FileNotFoundError:
            set_status("Error - Unable to read the apikey.config file", "red")
    else:
        with open(config_file_path, 'w') as file:
            file.write(f"# Paste your api key here\n{default_api_key}")
        api_key_entry.delete(0, 'end')
        api_key_entry.insert(0, default_api_key)

def paste_mod_id():
    clipboard_contents = window.clipboard_get()
    if clipboard_contents.isdigit():
        mod_id_entry.delete(0, 'end')
        mod_id_entry.insert(0, clipboard_contents)
    else:
        set_status("Invalid clipboard content. Mod ID must be a number.", "red")

window = tk.Tk()
window.title("Mod.io Downloader for SE - API")
window.geometry("350x200")
window.resizable(width=False, height=False)

api_key_label = tk.Label(window, text="Mod.io API Key:")
api_key_label.pack(fill='x')

api_key_entry = tk.Entry(window)
api_key_entry.pack(fill='x')

mod_id_label = tk.Label(window, text="Mod ID:")
mod_id_label.pack(fill='x')

mod_id_entry = tk.Entry(window)
mod_id_entry.pack(fill='x')

paste_button = tk.Button(window, text="Paste Mod ID from clipboard", command=paste_mod_id)
paste_button.pack()

download_button = tk.Button(window, text="Download Files", command=download_mod_files)
download_button.pack()

status_label = tk.Label(window, text="Status:", fg="black")
status_label.pack()

status_dynamic_label = tk.Label(window, text="")
status_dynamic_label.pack()

load_api_key_from_file()

window.mainloop()
