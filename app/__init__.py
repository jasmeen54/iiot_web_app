from flask import Flask, render_template, request, jsonify
from app.fetch_data import list_blob_data
from app.process_blob_data import process_blob_data
import json

app = Flask(__name__)

# Define route to list blob data
@app.route('/')
def list_blobs():
    # Load configuration
    blob_connection_string = ${{ secrets.AZURE_BLOB_STORAGE_CONNECTION_STRING }}
    container_name = 'dataiiot'

    
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






