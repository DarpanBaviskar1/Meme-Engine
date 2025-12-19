import json
import os

STORAGE_PATH = os.path.join(os.path.dirname(__file__), "memes_storage.json")

def load_memes():
    if os.path.exists(STORAGE_PATH):
        with open(STORAGE_PATH, "r") as f:
            return json.load(f)
    return []

def save_memes(memes):
    with open(STORAGE_PATH, "w") as f:
        json.dump(memes, f)

memes_storage = load_memes()
# print(memes_storage)