import boto3
import json
import time
import uuid
from datetime import datetime

# Initialize Kinesis client
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

# Function to generate log entries and push to Kinesis
def generate_log_entry():
    while True:
        log_data = {
            'request_id': str(uuid.uuid4()),   # Unique request ID
            'status_code': 200,  # Simulated HTTP status code (adjust as needed)
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp
        }
        # Send data to Kinesis
        kinesis_client.put_record(
            StreamName='log-streams',
            Data=json.dumps(log_data),
            PartitionKey=log_data['request_id']
        )
        print(f'Sent log: {log_data}')
        time.sleep(1)  # Send log entries every second (adjust interval as needed)

if __name__ == '__main__':
    generate_log_entry()
