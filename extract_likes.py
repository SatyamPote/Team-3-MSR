# extract_likes.py
import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from load import load_metric_to_sqlite

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_video_id(video_url):
    if "watch?v=" in video_url:
        return video_url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in video_url:
        return video_url.split("youtu.be/")[-1].split("?")[0]
    return None

def get_likes(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={API_KEY}"
    response = requests.get(url).json()
    if "items" in response and response["items"]:
        return int(response["items"][0]["statistics"].get("likeCount", 0))
    return 0

def extract_likes(video_url):
    video_id = get_video_id(video_url)
    if not video_id:
        print("❌ Invalid YouTube URL")
        return

    print("\n👍 Tracking likes every minute... Press Ctrl+C to stop.\n")
    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            likes = get_likes(video_id)

            load_metric_to_sqlite({
                "timestamp": timestamp,
                "video_id": video_id,
                "metric": "likes",
                "value": likes
            })

            print(f"❤️ Likes at {timestamp}: {likes}")
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n🛑 Stopped tracking likes.")
