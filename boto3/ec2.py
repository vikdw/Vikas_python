import boto3

# AWS_REGION = "us-east-1"
ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances()

instance_ids = []
volumes={}
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_ids.append(instance["InstanceId"])
        for block_device in instance.get('BlockDeviceMappings', []):
                volumes[instance["InstanceId"]]= (block_device['Ebs']['VolumeId'])

print(instance_ids)
print(volumes)