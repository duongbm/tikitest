import json
from src.config import STORAGE_FILE


def read_data():
    try:
        with open(STORAGE_FILE, 'r') as f:
            data = json.load(f)
        return data
    except:
        return None


def write(data):
    try:
        with open(STORAGE_FILE, 'w') as f:
            f.write(json.dumps(data))
        return True
    except:
        return False