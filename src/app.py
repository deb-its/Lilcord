import os
import json
import webview
from json import JSONDecodeError

storage_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Settings')
os.makedirs(storage_path, exist_ok=True) # Creates the folders if there's none
json_file_path = os.path.join(storage_path, 'config.json') 
if not os.path.exists(json_file_path): # If json is not created it will be created
    data = {"zoom": 1.0, "first_launch": True} 
    with open(json_file_path, 'w') as file:
        json.dump(data, file)

def initialize(window): # Set zoom
    try:
        with open(json_file_path, 'r') as file:
            zoom_data = json.load(file)
            saved_zoom = zoom_data.get('zoom', 1.0)
            window.evaluate_js(f"document.body.style.zoom = '{saved_zoom}';")
    except FileNotFoundError:
        pass

def get_url():
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
            
            if 'zoom' not in json_data: # Error handling BS (lines: 28-46)
                return "https://github.com/deb-its/Lilcord/blob/main/messages/error.md"
            
            if 'first_launch' not in json_data:
                return "https://github.com/deb-its/Lilcord/blob/main/messages/error.md"
            
            saved_zoom = json_data.get('zoom', 1.0)
            
            if json_data["first_launch"] and saved_zoom:
                json_data["first_launch"] = False
                with open(json_file_path, 'w') as write_file:
                    json.dump(json_data, write_file)
                return "https://github.com/deb-its/Lilcord/blob/main/messages/thankyou.md"
            else:
                return "https://discord.com/app"
    except FileNotFoundError:
        return "https://github.com/deb-its/Lilcord/blob/main/messages/error.md"
    except JSONDecodeError:
        return "https://github.com/deb-its/Lilcord/blob/main/messages/error.md"

if __name__ == '__main__':
    options = {'url': get_url(), 'width': 800, 'height': 600, 'resizable': True, 'fullscreen': False, 'easy_drag': True, 'confirm_close': True}
    window = webview.create_window('Lilcord', **options)
    webview.start(initialize, window, storage_path=storage_path)
