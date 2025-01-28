import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Function to start EC2 instance
def start_instance(instance_id):
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        print(f"Starting instance {instance_id}...")
        print(response)
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS credentials not configured properly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to stop EC2 instance
def stop_instance(instance_id):
    try:
        ec2_client = boto3.client('ec2')
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance {instance_id}...")
        print(response)
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS credentials not configured properly.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle start/stop
def main():
    instance_id = input("Enter the EC2 instance ID: ")
    action = input("Enter 'start' to start or 'stop' to stop the instance: ").strip().lower()

    if action == 'start':
        start_instance(instance_id)
    elif action == 'stop':
        stop_instance(instance_id)
    else:
        print("Invalid action. Please enter 'start' or 'stop'.")

if __name__ == "__main__":
    main()

