from flask import Flask, render_template, send_from_directory, jsonify
from app.fetch_data import list_and_fetch_blobs_in_container
from app.process_blob_data import process_blob_data
import os
import json
import threading
import time

app = Flask(__name__)

sensor_data = {}

def update_data():
    while True:
        blob_connection_string = os.environ.get('AZURE_BLOB_STORAGE_CONNECTION_STRING')
        container_name = os.environ.get('AZURE_CONTAINER_NAME')

        # List and fetch blobs in the container
        blobs_data = list_and_fetch_blobs_in_container(blob_connection_string, container_name)
        
        # Process blob data and organize it into sensor_data dictionary
        global sensor_data
        sensor_data = process_blob_data(blobs_data)

        # Print sensor_data for debugging
        print("Sensor Data:", sensor_data)

        # Wait for 10 minutes before next update
        time.sleep(600)

# Start the background data update thread
thread = threading.Thread(target=update_data)
thread.daemon = True
thread.start()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data')
def get_data():
    return jsonify(sensor_data)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)







