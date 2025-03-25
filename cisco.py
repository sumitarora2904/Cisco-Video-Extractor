import re
import requests
import warnings
import tkinter as tk
from tkinter import messagebox
import pyperclip
import webbrowser
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

# Function to validate the Cisco video URL
def validate_url(url):
    pattern = r"^https://video\.cisco\.com/detail/(video|videos/latest-videos/video)/(\d+)"
    match = re.match(pattern, url)
    if match:
        video_id = match.group(2)
        return video_id
    return None

# Function to fetch video data from the Brightcove API
def fetch_video_data(video_id):
    base_url = "https://edge.api.brightcove.com/playback/v1/accounts/1384193102001/videos/"
    final_url = f"{base_url}{video_id}"
    
    headers = {
        "Referer": "https://video.cisco.com/",
        "Origin": "https://video.cisco.com",
        "Authorization": "Bearer YOUR_ACCESS_TOKEN_HERE",  # Add your access token here
        "authority": "edge.api.brightcove.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "application/json;pk=BCpkADawqM2h963B1WkopB5Xr_hqKyZ269RAn-KyQghFHSMQ8nC6ulbB3o0DMkc_hAwOL-GS0bnA6mRRIrlcotzEmoDn60LOs3WG2_GuV5IWAy6NvYj5TrZ3QYKWrHt5dzhVBP6J1eVpd_Ou",
        "Accept-Encoding": "gzip, deflate, br, zstd"
    }
    
    try:
        response = requests.get(final_url, headers=headers, verify=False)
        if response.status_code == 200:
            data = response.json()
            video_url = extract_main_mp4_link(data)
            if video_url:
                return video_url
            else:
                return "Error: No 'main.mp4' URL found in the response."
        else:
            return f"Failed to fetch video data. Status Code: {response.status_code}"
    except Exception as e:
        return f"Error occurred while making the request: {e}"

# Function to extract the video URL
def extract_main_mp4_link(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict) and 'src' in item:
                        if 'main.mp4' in item['src']:
                            return item['src']
    return None

# Function to handle the video URL fetching process
def on_fetch_video():
    user_input = url_entry.get()
    video_id = validate_url(user_input)
    
    if video_id:
        result = fetch_video_data(video_id)
        if result.startswith("http"):
            # Display the video URL in the Text widget
            video_url_text.delete(1.0, tk.END)  # Clear the text box
            video_url_text.insert(tk.END, result)  # Insert the new video URL
            copy_button.config(state=tk.NORMAL)  # Enable the "Copy" button
            open_button.config(state=tk.NORMAL)  # Enable the "Open in Browser" button
        else:
            messagebox.showinfo("Error", result)
    else:
        messagebox.showerror("Error", "The link does not match the required format. Please try again.")

# Function to copy the video URL to the clipboard
def copy_to_clipboard():
    video_url = video_url_text.get(1.0, tk.END).strip()
    pyperclip.copy(video_url)  # Copy to clipboard
    messagebox.showinfo("Copied", "Video URL has been copied to clipboard!")

# Function to open the video URL in the browser
def open_in_browser():
    video_url = video_url_text.get(1.0, tk.END).strip()
    if video_url:
        webbrowser.open(video_url)  # Open the URL in the default web browser

# Set up the main window
window = tk.Tk()
window.title("Cisco Video Fetcher")

# Create a label
label = tk.Label(window, text="Enter the Cisco video link:")
label.pack(pady=10)

# Create a text entry widget for the URL
url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=10)

# Create a button to fetch the video URL
fetch_button = tk.Button(window, text="Fetch Video", command=on_fetch_video)
fetch_button.pack(pady=10)

# Create a Text widget to display the video URL
video_url_text = tk.Text(window, height=5, width=50, wrap=tk.WORD, padx=5, pady=5)
video_url_text.pack(pady=10)

# Create a "Copy to Clipboard" button (disabled initially)
copy_button = tk.Button(window, text="Copy Link", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=5)

# Create an "Open in Browser" button (disabled initially)
open_button = tk.Button(window, text="Open in Browser", command=open_in_browser, state=tk.DISABLED)
open_button.pack(pady=5)

# Run the application
window.mainloop()
