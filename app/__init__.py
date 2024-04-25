from flask import Flask, render_template, request, jsonify
from app.fetch_data import list_blob_data
from app.process_blob_data import process_blob_data
import json

app = Flask(__name__)

# Load configuration from config.json
def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config


# Define route to list blob data
@app.route('/')
def list_blobs():
    # Load configuration
    config = load_config()
    blob_connection_string = config.get('BLOB_CONNECTION_STRING')
    container_name = config.get('CONTAINER_NAME')

    
    # Retrieve blob data
    blob_data_list = list_blob_data(blob_connection_string, container_name)

    # Process blob data and organize it into sensor_data dictionary
    sensor_data = process_blob_data(blob_data_list)
    
    if sensor_data:
        return render_template("index.html", sensor_data=sensor_data)
    else:
        return "Error occurred while listing blob data."

if __name__ == '__main__':
    app.run(debug=True)






