# Roblox Status Notifier

**Roblox Status Notifier** is a lightweight Python application that tracks the presence status of a Roblox user in real time. It provides an easy-to-use interface for monitoring user activity such as whether they are online, in a game, in Roblox Studio, or offline, with options to receive notifications based on selected status changes.

## Features

- **Real-time User Status**: Continuously monitor the user's presence on Roblox (Online, In-Game, Invisible, etc.).
- **Customizable Notifications**: Select which statuses you want to receive notifications for.
- **Polling Mechanism**: Runs a background polling loop to check the user’s status at regular intervals.
- **User-Friendly Interface**: Built using Python's Tkinter library, offering a simple GUI to interact with the tool.
- **Logging**: Automatically logs system and user status information for debugging purposes.

## Requirements

- Python 3.x
- Pip (Python package manager; usually comes with Python)

## Installation

Install **Roblox Status Notifier** and run it locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/Xelvanta/roblox-statusnotifier.git
   cd roblox-statusnotifier
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the application:

```bash
python app.py
```

## Usage

Once the application is running, you will see a GUI with the following features:

- **User ID Input**: Enter the Roblox user ID you wish to track.
- **Status Display**: Displays the current status of the user (Online, In-Game, etc.).
- **Notification Checkboxes**: Choose which statuses you wish to be notified about.
- **Start and Stop Polling**: Start and stop the polling process with the provided buttons.

### Notifications

The application will notify you with a pop-up message when a user's status matches any of the selected notification preferences (e.g., when they go Online or In-Game).

---

## Code Overview

### Backend (API Requests)

The application communicates with Roblox’s **Presence API** to fetch the status of a user. Key components:

- **`fetch_user_presence()`**: Makes a POST request to Roblox's API and processes the user’s status.
- **Polling**: A separate thread continually checks the user’s status by calling the `fetch_user_presence()` method in intervals.

### Frontend (GUI)

The graphical user interface is built using **Tkinter**, which provides a simple interface to interact with the tool.

- **User ID Input**: Field to enter the Roblox user ID.
- **Status Display**: A label that shows the user’s current status.
- **Notification Toggles**: Checkboxes to select which statuses should trigger a notification.
- **Buttons**: Start/Stop polling buttons to control the status-checking process.

---

## Contributing

We welcome contributions! If you'd like to help improve **Roblox Status Notifier**, feel free to fork the repository, submit issues, and open pull requests. Please ensure that your code adheres to the existing style and passes all tests.

## License

**Roblox Status Notifier** is open source and available under the LICENSE included in the repository. See the LICENSE file for more details.

---

By **Xelvanta Group Systems**  
For support or inquiries, please contact us at [enquiry.information@proton.me](mailto:enquiry.information@proton.me).  
GitHub: [https://github.com/Xelvanta](https://github.com/Xelvanta)
