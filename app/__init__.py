from flask import Flask, render_template, send_from_directory
from .fetch_data import list_blobs_in_container
import os

app = Flask(__name__)

# Define route to list blobs
@app.route('/')
def list_blobs():
    # Load configuration
    blob_connection_string = os.environ.get('AZURE_BLOB_STORAGE_CONNECTION_STRING')
    container_name = 'dataiiot'

    # Log the environment variables for debugging
    print("Connection string:", blob_connection_string)
    print("Container name:", container_name)
    
    # Print container name
    print("Container name is:", container_name)
        
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

if __name__ == '__main__':
    app.run(debug=True)



