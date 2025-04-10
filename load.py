# load.py
import csv
import os
import sqlite3
from datetime import datetime

def load_to_csv(data, filename="output/movies_data.csv"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    write_header = not os.path.exists(filename)

    with open(filename, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Timestamp", "Title", "Year", "Rating"])
        if write_header:
            writer.writeheader()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for row in data:
            writer.writerow({
                "Timestamp": timestamp,
                **row
            })

def load_to_sqlite(data, db_file="output/movies.db"):
    os.makedirs(os.path.dirname(db_file), exist_ok=True)
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            title TEXT,
            year INTEGER,
            rating REAL
        )
    ''')

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for row in data:
        c.execute('''
            INSERT INTO movies (timestamp, title, year, rating)
            VALUES (?, ?, ?, ?)
        ''', (timestamp, row['Title'], row['Year'], row['Rating']))

    conn.commit()
    conn.close()
