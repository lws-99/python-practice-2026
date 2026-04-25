#This is the first programm of this series DSA with Python
#Author - Shyam D

import boto3

class EC2:
    def __init__(self):
        self.ec2 = boto3.resource("ec2", region_name="ap-south-1")

    def launch(self):
        self.ec2.create_instances(
            ImageId="ami-0e12ffc2dd465f6e4",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
        )
        print ("Instance launched")


obj = EC2()
obj.launch()