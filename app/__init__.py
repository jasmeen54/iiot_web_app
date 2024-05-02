from flask import Flask, render_template
from app.fetch_data import list_blobs_in_container
import json

app = Flask(__name__)

# Load configuration from config.json
def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

# Define route to list blobs
@app.route('/')
def list_blobs():
    # Load configuration
    config = load_config()
    blob_connection_string = config.get('BLOB_CONNECTION_STRING')
    container_name = config.get('CONTAINER_NAME')
    
    # List blobs in the container
    blobs = list_blobs_in_container(blob_connection_string, container_name)
    
    if blobs:
        return render_template("index.html", blobs=blobs)
    else:
        return "Error occurred while listing blobs."

if __name__ == '__main__':
    app.run(debug=True)





