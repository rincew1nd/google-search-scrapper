import json
import os

def save_file(content, filename):
    filepath = os.path.join('app/history', filename)
    with open(filepath, 'w') as json_file:
        json.dump(content, json_file, indent=4)