# config_loader.py

import json

def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

config = load_config()
blob_connection_string = config.get('BLOB_CONNECTION_STRING')
container_name = config.get('CONTAINER_NAME')
device_folders = config.get('DEVICE_FOLDERS')
