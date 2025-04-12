# main.py
from extract import extract_data

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    extract_data(video_url)
