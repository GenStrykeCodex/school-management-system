import json
import os

def load_data(file_path):

    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        return []

def save_data(file_path, data):

    directory = os.path.dirname(file_path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)