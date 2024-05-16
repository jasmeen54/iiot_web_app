from azure.storage.blob import BlobServiceClient
import json

def list_and_fetch_blobs_in_container(connection_string, container_name):
    try:
        if not connection_string:
            raise ValueError("Connection string is None.")
        
        print("Connecting to Blob Service...")
        # Create a BlobServiceClient using the connection string
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Get the container client for the specified container
        container_client = blob_service_client.get_container_client(container_name)
        
        # List blobs in the container and fetch data from JSON files
        blob_data_list = []
        for blob in container_client.list_blobs():
            # Check if the blob name ends with '.json'
            if blob.name.endswith('.json'):
                # Get the blob client for the current blob
                blob_client = container_client.get_blob_client(blob.name)
                # Download the blob data
                blob_data = blob_client.download_blob()
                # Read the blob data as a string
                data = blob_data.readall().decode('utf-8')
                # Append the blob data to the list
                blob_data_list.append(data)
        
        # Return the list of blob data
        return blob_data_list
    
    except Exception as e:
        # Print error message if an exception occurs
        print(f"Error listing and fetching blob data: {e}")
        return None










