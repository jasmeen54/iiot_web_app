from azure.storage.blob import BlobServiceClient
import json

def list_and_fetch_blobs_in_container(connection_string, container_name):
    try:
        if not connection_string:
            raise ValueError("Connection string is None.")
        
        print("Connecting to Blob Service...")
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        
        blobs_data = []

        # List all blobs and collect JSON data
        for blob in container_client.list_blobs():
            if blob.name.endswith('.json'):
                blob_client = container_client.get_blob_client(blob)
                blob_content = blob_client.download_blob().readall()
                blobs_data.append(blob_content)
        
        return blobs_data
    
    except Exception as e:
        print(f"Error listing and fetching blob data: {e}")
        return None










