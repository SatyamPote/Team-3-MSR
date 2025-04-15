# load.py
import os
import sqlite3

def load_metric_to_sqlite(data, db_file="output/video_metrics.db"):
    os.makedirs(os.path.dirname(db_file), exist_ok=True)
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS video_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            video_id TEXT,
            views INTEGER,
            likes INTEGER,
            comments INTEGER
        )
    ''')

    # Check if entry for this timestamp & video_id exists
    c.execute('''
        SELECT id FROM video_metrics
        WHERE timestamp = ? AND video_id = ?
    ''', (data["timestamp"], data["video_id"]))
    row = c.fetchone()

    if row:
        # Update only the relevant metric
        c.execute(f'''
            UPDATE video_metrics
            SET {data["metric"]} = ?
            WHERE id = ?
        ''', (data["value"], row[0]))
    else:
        # Insert new row with one metric, rest NULL
        c.execute(f'''
            INSERT INTO video_metrics (timestamp, video_id, {data["metric"]})
            VALUES (?, ?, ?)
        ''', (data["timestamp"], data["video_id"], data["value"]))

    conn.commit()
    conn.close()
