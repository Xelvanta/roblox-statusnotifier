import tkinter as tk
import requests
import threading
import time
import logging
from tkinter import messagebox
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

# Global variables for controlling polling
polling = False
poll_thread = None

def fetch_user_presence(user_id):
    url = "https://presence.roblox.com/v1/presence/users"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    payload = {
        "userIds": [user_id]
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        logging.debug(f"Request payload: {payload}")
        logging.debug(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            if 'userPresences' in data and len(data['userPresences']) > 0:
                user_presence = data['userPresences'][0]
                presence_type = user_presence['userPresenceType']
                logging.debug(f"User Presence Type: {presence_type}")
                
                # Update GUI with the presence data
                status_text.set(f"Status: {presence_type_text(presence_type)}\nResponse Code: {response.status_code}")
                
                # Check if the current status matches the notification flags
                if notify_flags[presence_type].get():
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get the current timestamp
                    messagebox.showinfo("Presence Notification", f"The user is now {presence_type_text(presence_type)}!\nTimestamp: {timestamp}")
            else:
                logging.debug("No user presence data found")
                status_text.set(f"Status: User not found or offline.\nResponse Code: {response.status_code}")
        else:
            logging.error(f"Failed to fetch presence data: {response.status_code}")
            status_text.set(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        status_text.set("Error: Request failed")

def presence_type_text(presence_type):
    presence_map = {
        0: "Offline",
        1: "Online",
        2: "In-Game",
        3: "In Studio",
        4: "Invisible"
    }
    return presence_map.get(presence_type, "Unknown")

def start_polling():
    global polling, poll_thread
    user_id = user_id_entry.get()
    if user_id.isdigit() and not polling:
        polling = True
        poll_thread = threading.Thread(target=poll_presence, args=(int(user_id),))
        poll_thread.daemon = True  # Allow thread to be killed when main program ends
        poll_thread.start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
    else:
        status_text.set("Error: Please enter a valid user ID or polling is already active.")

def stop_polling():
    global polling
    polling = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

def poll_presence(user_id):
    while polling:
        fetch_user_presence(user_id)
        time.sleep(1)

# GUI Setup
root = tk.Tk()
root.title("Roblox Presence Checker")

window_width = 400
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

tk.Label(root, text="Enter User ID:").pack(pady=10)

user_id_entry = tk.Entry(root)
user_id_entry.pack(pady=5)

start_button = tk.Button(root, text="Start Polling", command=start_polling)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Polling", command=stop_polling, state=tk.DISABLED)
stop_button.pack(pady=10)

status_text = tk.StringVar()
status_label = tk.Label(root, textvariable=status_text, justify=tk.LEFT)
status_label.pack(pady=10)

# Now create the notify_flags after initializing the root
notify_flags = {
    0: tk.BooleanVar(value=False),  # Offline
    1: tk.BooleanVar(value=False),  # Online
    2: tk.BooleanVar(value=False),  # In-Game
    3: tk.BooleanVar(value=False),  # In Studio
    4: tk.BooleanVar(value=False)   # Invisible
}

# Presence Status Notification Toggles
checkbox_label = tk.Label(root, text="Select statuses you want to be notified about:")
checkbox_label.pack(pady=5)

status_frame = tk.Frame(root)
status_frame.pack(pady=10)

for presence_type, flag in notify_flags.items():
    tk.Checkbutton(status_frame, text=presence_type_text(presence_type), variable=flag).pack(side=tk.LEFT)

root.mainloop()