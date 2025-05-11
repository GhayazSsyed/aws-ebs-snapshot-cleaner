import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # List all EBS snapshots owned by this account
    response = ec2.describe_snapshots(OwnerIds=['self'])

    # Get all active (running) EC2 instance IDs
    instance_response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )

    active_instance_ids = set()
    for reservation in instance_response['Reservations']:
        for instance in reservation['Instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot
    for snapshot in response['Snapshots']:  # Fix: Should be 'Snapshots', not 'SnapshotId'
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get('VolumeId')

        if not volume_id:
            ec2.delete_snapshot(SnapshotId=snapshot_id)  # Fix: Use the variable, not a string literal
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
        else:
            try:
                # Check if volume exists and get its attachment details
                volume_response = ec2.describe_volumes(VolumeIds=[volume_id])  # Fix: Proper argument structure
                attachments = volume_response['Volumes'][0].get('Attachments', [])

                # If the volume is not attached to any running instance
                attached_instance_ids = {attachment['InstanceId'] for attachment in attachments}
                if not attached_instance_ids & active_instance_ids:  # no intersection means unused
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")

            except ec2.exceptions.ClientError as e:
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")
