from flask import Flask, render_template
from app.fetch_data import list_blob_data
from app.process_blob_data import process_blob_data
import json
import os
import logging

# Set logging configuration
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG

app = Flask(__name__)

# Define a logger
logger = logging.getLogger(__name__)

# Load configuration from config.json
#def load_config():
    #with open('config.json', 'r') as f:
        #config = json.load(f)
    #return config

# Define route to list blob data
@app.route('/')
def list_blobs():
    # Load configuration
    #config = load_config()
    #blob_connection_string = config.get('BLOB_CONNECTION_STRING')
    #container_name = config.get('CONTAINER_NAME')
    
    blob_connection_string = os.environ.get('AZURE_BLOB_STORAGE_CONNECTION_STRING')
    container_name = os.environ.get('AZURE_CONTAINER_NAME')

    # Log the connection string and container name
    logger.debug(f'Blob Connection String: {blob_connection_string}')
    logger.debug(f'Container Name: {container_name}')

    # Retrieve blob data
    blob_data_list = list_blob_data(blob_connection_string, container_name)

    # Log the number of blobs retrieved
    logger.debug(f'Number of Blobs Retrieved: {len(blob_data_list)}')

    # Process blob data and organize it into sensor_data dictionary
    sensor_data = process_blob_data(blob_data_list)
    
    if sensor_data:
        return render_template("index.html", sensor_data=sensor_data)
    else:
        return "Error occurred while listing blob data."

if __name__ == '__main__':
    app.run(debug=True)






