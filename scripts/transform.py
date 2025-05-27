import json
import os
import pandas as pd

RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"
os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
def load_and_transform():
    all_logs = []

    for filename in os.listdir(RAW_DATA_PATH):
        if filename.endswith(".json"):
            file_path = os.path.join(RAW_DATA_PATH, filename)
            with open(file_path, "r") as f:
                try:
                    data = json.load(f)
                    all_logs.append(data)
                except json.JSONDecodeError:
                    print(f"Skipping corrupted file: {filename}")

    if not all_logs:
        print("No valid logs found.")
        return

    df = pd.DataFrame(all_logs)
    df['view_time'] = pd.to_datetime(df['view_time'])  # Standardize timestamp

    output_path = os.path.join(PROCESSED_DATA_PATH, "transformed_logs.csv")
    df.to_csv(output_path, index=False)
    print(f"[✓] Transformed data written to {output_path}")

if __name__ == "__main__":
    load_and_transform()
