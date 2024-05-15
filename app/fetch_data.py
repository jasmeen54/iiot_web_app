# app/fetch_data.py
from azure.storage.blob import BlobServiceClient

def list_blobs_in_container(connection_string, container_name):
    try:
        print("Connecting to Blob Service...")
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        print(f"Getting container client for {container_name}...")
        container_client = blob_service_client.get_container_client(container_name)
        
        # Dictionary to hold blobs per folder
        blobs_in_folders = {}

        # List blobs in the container for each iiotdevice folder
        for i in range(1, 21):  # Assuming there are 20 iiotdevice folders
            prefix = f'iiotdevice{i:02d}/'  # Format as iiotdevice01, iiotdevice02, etc.
            blobs_in_folders[prefix] = []
            print(f"Listing blobs with prefix: {prefix}")
            for blob in container_client.list_blobs(name_starts_with=prefix):
                print(f"Found blob: {blob.name}")
                if blob.name.endswith('.json'):
                    blobs_in_folders[prefix].append(blob.name)
        
        print("Blobs in folders:", blobs_in_folders)
        return blobs_in_folders
    
    except Exception as e:
        print(f"Error listing blob names: {e}")
        return None










