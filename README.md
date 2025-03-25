# Cisco-Video-Extractor
This Python script extracts video data (direct video URL) from Cisco video links.


## Features

- Validates Cisco video URLs.
- Extracts the video ID from the URL.
- Fetches video data using the Brightcove API.
- Retrieves the `main.mp4` URL for video playback.

## Supported URL Formats

- **Old format**:  
  `https://video.cisco.com/detail/video/{video_id}`

- **New format**:  
  `https://video.cisco.com/detail/videos/latest-videos/video/{video_id}?autoStart=true`

## Prerequisites

- Python 3.x
- `requests` library
- You need to obtain a valid access token from Brightcove to access the API.

### Installing Dependencies

To install the required dependencies, run the following command:

`pip install requests`

## Setup

1. Clone this repository to your local machine:
   
   `git clone https://github.com/yourusername/cisco-video-extractor.git`

4. Change to the project directory:

   `cd cisco-video-extractor`

## Usage

1. Run the script:
  
   `python video_extractor.py`

2. When prompted, input the Cisco video URL. For example:

   - Old format: `https://video.cisco.com/detail/video/6327222704112`
   - New format: `https://video.cisco.com/detail/videos/latest-videos/video/6370206110112?autoStart=true`

3. The script will validate the URL, fetch the video data, and print the `main.mp4` video URL if found.

## Example

### Input:
```
Please enter the Cisco video link (e.g., https://video.cisco.com/detail/video/6327222704112):
https://video.cisco.com/detail/videos/latest-videos/video/6370206110112?autoStart=true
```

### Output:
```
Valid URL entered! Video ID: 6370206110112
Found video URL: https://path-to-video/main.mp4
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The script uses the Brightcove API for fetching video data.
- The regular expression used to validate URLs was created based on Cisco's video URL structure.
