from azure.storage.blob import BlobServiceClient
import os
import json

def list_blobs_in_container(blob_connection_string, container_name):
    try:
        # Connect to the Blob Service
        blob_service_client = BlobServiceClient.from_connection_string(blob_connection_string)

        # Get a reference to the container
        container_client = blob_service_client.get_container_client(container_name)

        # List blobs in the container
        blobs = [blob.name for blob in container_client.list_blobs()]
        return blobs

    except Exception as e:
        print(f"Error listing blobs in container: {e}")
        return None










