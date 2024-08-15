import boto3
class SageMakerDeployer:
    def __init__(self, role, image_uri):
        self.sm = boto3.client('sagemaker')
        self.role = role
        self.image_uri = image_uri
    def create_model(self, model_name, model_url):
        return self.sm.create_model(ModelName=model_name, PrimaryContainer={'Image': self.image_uri, 'ModelDataUrl': model_url}, ExecutionRoleArn=self.role)
    def create_endpoint(self, endpoint_name, config_name):
        return self.sm.create_endpoint(EndpointName=endpoint_name, EndpointConfigName=config_name)
