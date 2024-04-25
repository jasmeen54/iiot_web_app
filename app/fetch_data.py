from azure.storage.blob import BlobServiceClient
import json

def list_blob_data(connection_string, container_name):
    try:
        # Connect to the Blob Service
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Get a reference to the container
        container_client = blob_service_client.get_container_client(container_name)
        
        # List blobs in the container
        blob_data_list = []
        for blob in container_client.list_blobs():
            if blob.name.endswith('.json'):
                blob_client = container_client.get_blob_client(blob.name)
                blob_data = blob_client.download_blob()
                data = blob_data.readall().decode('utf-8')
                blob_data_list.append(data)
        
        return blob_data_list
    
    except Exception as e:
        print(f"Error listing blob data: {e}")
        return None












