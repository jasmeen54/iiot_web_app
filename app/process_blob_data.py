import json

def process_blob_data(blob_data_list):
    try:
        sensor_data = {}

        for blob_data in blob_data_list:
            # Parse the JSON data
            json_data = json.loads(blob_data)

            # Extract sensor name from the JSON data
            sensor_name = json_data.get('sensor')

            # Initialize data list for the sensor if not exists
            if sensor_name not in sensor_data:
                sensor_data[sensor_name] = {"data": [], "stats": {}}

            # Extract value and timestamp from the JSON data
            value = json_data.get('value')
            timestamp = json_data.get('timestamp')

            # Append value and timestamp to sensor data list
            sensor_data[sensor_name]["data"].append({
                "value": value,
                "timestamp": timestamp
            })

        # Calculate statistics for each sensor
        for sensor_name, sensor_info in sensor_data.items():
            data_list = sensor_info["data"]
            values = [item["value"] for item in data_list]

            if values:
                avg_value = sum(values) / len(values)
                max_value = max(values)
                min_value = min(values)
                sensor_data[sensor_name]["stats"] = {
                    "average": avg_value,
                    "max": max_value,
                    "min": min_value
                }

            # Sort sensor data by timestamp
            sensor_data[sensor_name]["data"] = sorted(data_list, key=lambda x: x["timestamp"])

        return sensor_data

    except Exception as e:
        print(f"Error processing blob data: {e}")
        return None


