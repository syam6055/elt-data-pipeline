import pandas as pd
import sqlite3
import os

CSV_PATH = "data/processed/transformed_logs.csv"
DB_PATH = "data/processed/logs.db"

def load_to_sqlite():
    if not os.path.exists(CSV_PATH):
        print("CSV file not found")
        return
    
    df = pd.read_csv(CSV_PATH)
    
    conn = sqlite3.connect(DB_PATH)
    
    df.to_sql("video_views", conn, if_exists='replace', index=False)
    
    print(f"[✓] Data {len(df)} records into SQLite database at {DB_PATH}")
    conn.close()
    
if __name__ == "__main__":
    load_to_sqlite()
    