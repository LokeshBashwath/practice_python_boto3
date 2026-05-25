import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

# Describe instances with a filter for 'running' state
response = ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

print("Running Instances:")
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"ID: {instance['InstanceId']} | Type: {instance['InstanceType']}")
