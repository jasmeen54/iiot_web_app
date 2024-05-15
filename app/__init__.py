from flask import Flask, render_template
from app.fetch_data import list_blobs_in_container
import json

app = Flask(__name__)

@app.route('/')
def list_blobs():
    # Load configuration
    blob_connection_string = os.environ.get('AZURE_BLOB_STORAGE_CONNECTION_STRING')
    container_name = 'dataiiot'

    # Print container name and connection string for debugging
    print("Connection string is:", blob_connection_string)
    print("Container name is:", container_name)
    
    # Check if environment variables are None
    if not blob_connection_string:
        return "Error: AZURE_BLOB_STORAGE_CONNECTION_STRING environment variable not set."
    if not container_name:
        return "Error: AZURE_CONTAINER_NAME environment variable not set."

    # List blobs in the container
    blobs = list_blobs_in_container(blob_connection_string, container_name)

    # Print blobs to the console for debugging
    print("Blobs retrieved from Azure Blob Storage:", blobs)

    if blobs:
        return render_template("index.html", blobs=blobs)
    else:
        return "No blobs found in the container."

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')





