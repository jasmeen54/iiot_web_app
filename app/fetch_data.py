from azure.storage.blob import BlobServiceClient
import json

def list_and_fetch_blobs_in_container(connection_string, container_name):
    try:
        if not connection_string:
            raise ValueError("Connection string is None.")
        
        print("Connecting to Blob Service...")
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)
        
        blobs_data = {}
        unique_prefixes = set()

        # List all blobs and collect unique prefixes
        for blob in container_client.list_blobs():
            if '/' in blob.name:
                prefix = blob.name.split('/')[0] + '/'
                unique_prefixes.add(prefix)
        
        # For each unique prefix, fetch JSON data from blobs
        for prefix in unique_prefixes:
            blobs_data[prefix] = {}
            for blob in container_client.list_blobs(name_starts_with=prefix):
                if blob.name.endswith('.json'):
                    blob_client = container_client.get_blob_client(blob)
                    blob_content = blob_client.download_blob().readall()
                    blobs_data[prefix][blob.name] = json.loads(blob_content)
        
        return blobs_data
    
    except Exception as e:
        print(f"Error listing and fetching blob data: {e}")
        return None












