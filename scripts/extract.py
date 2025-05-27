import json
import os
import random
import time
from datetime import datetime
from faker import Faker

fake = Faker()
RAW_DATA_PATH = "data/raw/"
os.makedirs(RAW_DATA_PATH, exist_ok=True)

def generate_video_log():
    return {
        "video_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "region": random.choice(["US", "IN", "UK", "JP", "BR"]),
        "device_type": random.choice(["iOS", "Android", "Web"]),
        "caption": fake.sentence(nb_words=6),
        "view_time": datetime.utcnow().isoformat()
    }

def stream_logs(n=10, delay=1):
    for i in range(n):
        log = generate_video_log()
        file_path = os.path.join(RAW_DATA_PATH, f"log_{int(time.time())}.json")
        with open(file_path, "w") as f:
            json.dump(log, f)
        print(f"[✓] Log written: {file_path}")
        time.sleep(delay)

if __name__ == "__main__":
    stream_logs(n=10, delay=1)
