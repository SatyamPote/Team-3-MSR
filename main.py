import time
from extract import extract_imdb_data
from datetime import datetime

def run_every_minute():
    while True:
        print("\n" + "=" * 50)
        print(f"🚀 Running at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        extract_imdb_data()
        time.sleep(60)

if __name__ == "__main__":
    print("🟢 IMDB movie fetch started. Auto-saving CSV every 1 minute...\nPress Ctrl+C to stop.")
    run_every_minute()
