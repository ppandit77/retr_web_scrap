# NightOwl Branch Data Fetcher

This project helps you fetch branch details from retr.app and save them to a CSV file. It is designed for beginners and includes step-by-step instructions.

## Prerequisites
- Python 3.7 or higher installed on your computer
- Google Chrome or another web browser
- Internet connection

## Step 1: Get Your Cookie from retr.app
To access the data, you need to copy your session cookie from retr.app. Here’s how:

1. **Log in to retr.app** in your browser.
2. **Open Developer Tools**:
   - Press `F12` or right-click anywhere on the page and select `Inspect`.
3. Go to the **Network** tab.
4. Refresh the page or perform the action that loads the data you want.
5. Click on any network request (e.g., `GetLOsByBranch`).
6. In the right panel, go to the **Headers** tab.
7. Scroll down to **Request Headers** and find the line starting with `cookie:`.
8. **Copy the entire cookie value** (everything after `cookie:`).
9. Open `fetch_details_from_header.py` in a text editor and replace the value of the `"cookie"` key in the `headers` dictionary with your copied cookie.

> **Tip:** If you log out or your session expires, you will need to repeat these steps to get a fresh cookie.

## Step 2: Set Up Python
1. Download and install Python from [python.org](https://www.python.org/downloads/) if you don’t have it.
2. Open a terminal (Command Prompt or PowerShell on Windows).
3. (Optional but recommended) Create a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```

## Step 3: Install Required Packages
Install the required Python packages using pip:
```sh
pip install requests
```

## Step 4: Run the Script
1. Make sure you are in the project directory (where `fetch_details_from_header.py` is located).
2. Run the script:
   ```sh
   python fetch_details_from_header.py
   ```
3. The script will:
   - Fetch branch data from retr.app
   - Print the response
   - Save the data to a file called `branches.csv`

## Step 5: View the Output
- Open `branches.csv` in Excel, Google Sheets, or any spreadsheet program to view the branch data.

## Troubleshooting
- **No data in CSV?**
  - Make sure your cookie is up to date and you are logged in to retr.app.
  - Try refreshing your session and copying the cookie again.
  - Check your internet connection.
- **Script errors?**
  - Make sure you have installed the `requests` package.
  - Make sure you are using Python 3.7 or higher.
- **Still not working?**
  - Double-check that you copied the entire cookie string.
  - Some data may be restricted based on your user permissions on retr.app.

## Customization
- To change the search term or state, edit the `payload` variable in `fetch_details_from_header.py`.
- To save the CSV with a different name, change the filename in the script.

---

If you have any questions or need help, feel free to ask!
