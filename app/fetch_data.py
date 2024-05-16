from azure.storage.blob import BlobServiceClient
import os

def list_blobs_in_container(connection_string, container_name):
    try:
        if not connection_string:
            raise ValueError("Connection string is None.")
        
        print("Connecting to Blob Service...")
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        
        blobs_in_folders = {}
        unique_prefixes = set()

        # List all blobs and collect unique prefixes
        for blob in container_client.list_blobs():
            # Assuming folder names end with a '/'
            if '/' in blob.name:
                prefix = blob.name.split('/')[0] + '/'
                unique_prefixes.add(prefix)
        
        # For each unique prefix, list blobs that end with .json
        for prefix in unique_prefixes:
            blobs_in_folders[prefix] = []
            for blob in container_client.list_blobs(name_starts_with=prefix):
                if blob.name.endswith('.json'):
                    blobs_in_folders[prefix].append(blob.name)
        
        return blobs_in_folders
    
    except Exception as e:
        print(f"Error listing blob names: {e}")
        return None












