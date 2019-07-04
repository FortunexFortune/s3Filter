import boto3


class Bucket:

    name = ''

    def __init__(self, name):
        self.name = name

    def getUavs(self):
        client = boto3.client('s3')
        response = client.list_objects(Bucket=self.name)
        uavs = response.get('Contents')
        return uavs