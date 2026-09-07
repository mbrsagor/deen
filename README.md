# Eye Care Break Timer Extension

A lightweight Google Chrome extension designed to help reduce eye strain by reminding you to take breaks at regular intervals. 

## Features
- **Dynamic Work Time:** Set how many minutes you want to work before taking a break (e.g., 20 minutes).
- **Dynamic Break Time:** Set how long your break should be (e.g., 2 minutes).
- **Automated Cycle:** Automatically starts the break timer after your work time, and restarts the work timer when your break is over.
- **Desktop Notifications:** Provides system-level notifications so you don't miss your break, even if Chrome is in the background.

## How to Install (Developer Mode)
1. Download or clone this repository to your local machine.
2. Open Google Chrome and navigate to `chrome://extensions/`.
3. Enable **Developer mode** using the toggle switch in the top right corner.
4. Click the **Load unpacked** button in the top left corner.
5. Select the folder containing these extension files (the `eyeCare` folder).
6. The extension icon will appear in your Chrome toolbar.

## Usage
1. Click the extension icon in your Chrome toolbar.
2. Enter your desired **Work Time** (in minutes).
3. Enter your desired **Break Time** (in minutes).
4. Click **Save & Restart Timer**.
5. You will receive a notification when it is time to look away from your screen!

## Project Structure
- `manifest.json`: The configuration and permissions for the Chrome extension.
- `background.js`: The background service worker that manages the alarms and notifications.
- `popup.html`: The user interface for the settings menu.
- `popup.js`: The logic for saving and loading user settings.
- `icon.png`: The extension icon.
