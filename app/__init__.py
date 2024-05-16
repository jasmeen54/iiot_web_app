from flask import Flask, render_template, send_from_directory, jsonify
from app.fetch_data import list_and_fetch_blobs_in_container
from app.process_blob_data import process_blob_data
import os
import json
import threading
import time

app = Flask(__name__)

# Initialize sensor_data as an empty dictionary
sensor_data = {}
sensor_data_lock = threading.Lock()  # Create a lock for synchronization

def update_data():
    while True:
        blob_connection_string = os.environ.get('AZURE_BLOB_STORAGE_CONNECTION_STRING')
        container_name = os.environ.get('AZURE_CONTAINER_NAME')

        # List and fetch blobs in the container
        blobs_data = list_and_fetch_blobs_in_container(blob_connection_string, container_name)
        
        # Process blob data and organize it into sensor_data dictionary
        processed_data = process_blob_data(blobs_data)

        # Acquire the lock before updating sensor_data
        with sensor_data_lock:
            sensor_data.clear()  # Clear existing data
            sensor_data.update(processed_data)  # Update with new data

        # Wait for 5 minutes before next update
        time.sleep(300)

# Start the background data update thread
thread = threading.Thread(target=update_data)
thread.daemon = True
thread.start()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data')
def get_data():
    global sensor_data
    # Acquire the lock before accessing sensor_data
    with sensor_data_lock:
        sensor_data_json = json.dumps(sensor_data)
        return sensor_data_json

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)





