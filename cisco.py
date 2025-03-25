import re
import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

def validate_url(url):
    # Regular expression to match both old and new URL formats and extract the video ID
    pattern = r"^https://video\.cisco\.com/detail/(video|videos/latest-videos/video)/(\d+)"
    match = re.match(pattern, url)
    if match:
        video_id = match.group(2)  # Capture the video ID
        return video_id
    else:
        return None

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
            data = response.json()  # Parse the JSON response
            video_url = extract_main_mp4_link(data)  # Extract the video URL
            if video_url:
                print(f"Found video URL: {video_url}")
            else:
                print("Error: No 'main.mp4' URL found in the response.")
        else:
            print(f"Failed to fetch video data. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while making the request: {e}")

def extract_main_mp4_link(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, dict) and 'src' in item:
                        if 'main.mp4' in item['src']:  # Look for 'main.mp4' in the source URL
                            return item['src']
    return None

def main():
    user_input = input("Please enter the Cisco video link (e.g., https://video.cisco.com/detail/video/6327222704112): ")
    video_id = validate_url(user_input)  # Validate the URL and extract the video ID
    
    if video_id:
        print(f"Valid URL entered! Video ID: {video_id}")
        fetch_video_data(video_id)  # Fetch and process video data using the video ID
    else:
        print("Error: The link does not match the required format. Please try again.")

if __name__ == "__main__":
    main()  # Start the script execution
