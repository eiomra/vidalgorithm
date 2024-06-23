import json

def parse_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['users'], data['videos']
