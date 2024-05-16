from flask import Flask, render_template, send_from_directory
from app.fetch_data import list_and_fetch_blobs_in_container
from app.process_blob_data import process_blob_data
import os

app = Flask(__name__)

# Define route to list and display blobs
@app.route('/')
def list_blobs():
    # Load configuration
    blob_connection_string = os.environ.get('AZURE_BLOB_STORAGE_CONNECTION_STRING')
    container_name = os.environ.get('AZURE_CONTAINER_NAME')

    # Print container name and connection string for debugging
    print("Connection string is:", blob_connection_string)
    print("Container name is:", container_name)
    
    # Check if environment variables are None
    if not blob_connection_string:
        return "Error: AZURE_BLOB_STORAGE_CONNECTION_STRING environment variable not set."
    if not container_name:
        return "Error: AZURE_CONTAINER_NAME environment variable not set."

    # List and fetch blobs in the container
    blobs_data = list_and_fetch_blobs_in_container(blob_connection_string, container_name)
    
    # Process blob data and organize it into sensor_data dictionary
    sensor_data = process_blob_data(blobs_data)

    # Check if sensor_data is None
    if sensor_data is None:
        return "Error occurred while processing blob data."

    # Convert sensor_data to JSON string
    sensor_data_json = json.dumps(sensor_data)

    # Render the template with sensor data
    return render_template("index.html", sensor_data_json=sensor_data_json)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)




