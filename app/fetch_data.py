from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

def list_blobs_in_container(connection_string, container_name):
    try:
        if not connection_string:
            raise ValueError("Connection string is None.")
        
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        
        blobs_in_folders = {}
        for i in range(1, 21):
            prefix = f'iiotdevice{i:02d}/'
            blobs_in_folders[prefix] = []
            for blob in container_client.list_blobs(name_starts_with=prefix):
                if blob.name.endswith('.json'):
                    blobs_in_folders[prefix].append(blob.name)
        return blobs_in_folders
    
    except Exception as e:
        print(f"Error listing blob names: {e}")
        return None











