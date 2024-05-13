from flask import Flask, render_template
from app.fetch_data import list_blobs_in_container
import json
import os

app = Flask(__name__)

# Define route to list blobs
@app.route('/')
def list_blobs():
    try:
        # Load configuration
        blob_connection_string = os.environ.get('AZURE_BLOB_STORAGE_CONNECTION_STRING')
        container_name = os.environ.get('AZURE_CONTAINER_NAME')
        
        # List blobs in the container
        blobs = list_blobs_in_container(blob_connection_string, container_name)
        
        if blobs:
            return render_template("index.html", blobs=blobs)
        else:
            return "No blobs found in the container."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)





