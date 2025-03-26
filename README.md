# Cisco-Video-Extractor

This Python script extracts video data (direct video URL) from Cisco video links using a graphical user interface (GUI). The script allows users to input a Cisco video URL, validate it, fetch video data, and either copy the video URL to the clipboard or open it directly in a web browser.

## Features

- **Validates Cisco video URLs**.
- **Extracts the video ID** from the URL.
- **Fetches video data** using the Brightcove API.
- Retrieves the `main.mp4` URL for video playback.
- **GUI Interface** built with **Tkinter**:
  - Input Cisco video URL.
  - Display the extracted video URL.
  - Copy the video URL to clipboard.
  - Open the video URL in a web browser.

## Prerequisites

- Python 3.x
- `requests` library
- `pyperclip` library (for clipboard functionality)
- Tkinter (should be included with Python by default)

### Installing Dependencies

To install the required dependencies, run the following commands:

```bash
pip install requests
pip install pyperclip
```

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sumitarora2904/cisco-video-extractor.git
   ```

2. Change to the project directory:

   ```bash
   cd cisco-video-extractor
   ```

## Usage

1. Run the script:

   ```bash
   python cisco.py
   ```

2. The Tkinter-based GUI will appear. Enter the Cisco video URL in the provided text field. For example:

   - Old format: `https://video.cisco.com/detail/video/6327222704112`
   - New format: `https://video.cisco.com/detail/videos/latest-videos/video/6370206110112?autoStart=true`

3. The script will:
   - Validate the URL.
   - Fetch the video data using the Brightcove API.
   - Display the `main.mp4` video URL in the text box.
   - Enable buttons to **Copy** the URL to your clipboard or **Open** the URL in a web browser.

### Example

#### Input:

```
Please enter the Cisco video link:
https://video.cisco.com/detail/videos/latest-videos/video/6370206110112?autoStart=true
```

#### Output:

- The `main.mp4` URL will be displayed in the text box.
- The **Copy Link** button will copy the video URL to the clipboard.
- The **Open in Browser** button will open the video in your default browser.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The script uses the **Brightcove API** for fetching video data.
- The regular expression used to validate URLs was created based on Cisco's video URL structure.
- The GUI is created with **Tkinter** for better user experience.
