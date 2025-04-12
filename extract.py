# extract.py
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env
API_KEY = os.getenv("API_KEY")

import requests
import time
import csv
import os
from datetime import datetime
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_video_id(video_url):
    if "watch?v=" in video_url:
        return video_url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in video_url:
        return video_url.split("youtu.be/")[-1].split("?")[0]
    return None

def get_video_statistics(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={API_KEY}"
    response = requests.get(url).json()
    if "items" in response and response["items"]:
        stats = response["items"][0]["statistics"]
        return int(stats.get("likeCount", 0)), int(stats.get("commentCount", 0))
    return 0, 0

def extract_data(video_url):
    video_id = get_video_id(video_url)

    if not video_id:
        print("Invalid YouTube URL")
        return

    print("\n⏳ Collecting data every 1 minute... Press Ctrl+C to stop.\n")

    try:
        while True:
            timestamp = datetime.now().strftime("%j-%H-%M-%S")
            likes, comments = get_video_statistics(video_id)

            filename = f"imdb_{timestamp}.csv"
            with open(filename, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Video ID", "Likes", "Total Comments"])
                writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), video_id, likes, comments])

            print(f"✅ Data saved to {filename} at {datetime.now().strftime('%H:%M:%S')}")
            time.sleep(60)

    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")
