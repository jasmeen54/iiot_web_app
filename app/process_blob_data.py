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
                sensor_data[sensor_name] = {
                    "data": [],
                    "average_value": 0  # Initialize average value
                }

            # Extract value and timestamp from the JSON data
            value = json_data.get('value')
            timestamp = json_data.get('timestamp')

            # Check if the value contains a percentage sign
            if '%' in value:
                # For percentage values, remove the percentage sign and convert to float
                numerical_value = float(value.replace('%', ''))
            else:
                # For other values, extract the numerical part and convert to float
                numerical_value = float(value.split()[0])

            # Append value and timestamp to sensor data list
            sensor_data[sensor_name]["data"].append({
                "value": numerical_value,
                "timestamp": timestamp
            })

        # Calculate average value for each sensor
        for sensor_name, data in sensor_data.items():
            data_list = data["data"]
            if data_list:
                values = [d["value"] for d in data_list]
                average_value = sum(values) / len(values)
                sensor_data[sensor_name]["average_value"] = average_value

        return sensor_data

    except Exception as e:
        print(f"Error processing blob data: {e}")
        return None
