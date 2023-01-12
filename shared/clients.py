import boto3

class ClientFactory:

    def __init__(self, profile_name, region_name):
        self.profile_name = profile_name
        self.region_name = region_name
        self.session = boto3.Session(
            profile_name=profile_name,
            region_name=region_name
        )
    
    def create_client(self, service):
        return self.session.client(service)

    def create_connect_client(self):
        self.connect_client = self.create_client('connect')

