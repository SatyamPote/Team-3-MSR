import time
from datetime import datetime
from extract import extract_imdb_data

def run_every_minute():
    print("Starting fetch every 1 minute...\nPress Ctrl+C to stop.\n")
    try:
        while True:
            print("="*50)
            print(f"Running at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            extract_imdb_data()
            print("Waiting for 60 seconds...\n")
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    run_every_minute()
