# main.py
import time
from datetime import datetime
from extract import extract_imdb_data
from transform import transform_movies_data
from load import load_to_csv, load_to_sqlite

def run_etl_pipeline():
    print(f"\n{'-'*40}")
    print(f"ETL Cycle Started: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    try:
        # Extract
        raw_data = extract_imdb_data()
        if not raw_data:
            print("❌ No data extracted")
            return

        # Transform
        clean_data = transform_movies_data(raw_data)
        if not clean_data:
            print("❌ Transformation returned no valid records")
            return

        # Load
        load_to_csv(clean_data)
        load_to_sqlite(clean_data)

        print(f"✅ ETL Cycle Completed Successfully")
    
    except Exception as e:
        print(f"❗ ETL Pipeline Error: {str(e)}")
    
    finally:
        print(f"{'-'*40}\n")

if __name__ == "__main__":
    # Run pipeline every X minutes
    INTERVAL_MINUTES = 1  # ⏱️ Set to 1 minute or change as needed
    while True:
        run_etl_pipeline()
        time.sleep(INTERVAL_MINUTES * 60)
