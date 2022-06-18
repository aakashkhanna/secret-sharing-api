import boto3
import uuid
from datetime import datetime, timedelta
import json
from secret_sharing_api.models.create_secret import CreateSecretRequest
from secret_sharing_api.models.secret import Secret
from secret_sharing_api.services.config_service import get_configs

class DynamoDataService():
    def __init__(self, dynamo_db_client = None):
        self.config = get_configs()
        if dynamo_db_client is None:
            self.dynamo_db_client =  boto3.resource(
                'dynamodb', 
                endpoint_url=self.config.aws_endpoint_url, 
                region_name=self.config.aws_region_name,
                aws_access_key_id=self.config.aws_access_key_id,
                aws_secret_access_key=self.config.aws_secret_access_key) 
    
    def get_secrets_table(self):
        table = self.dynamo_db_client.Table(self.config.aws_dynamo_name)
        return table

    def add_secret(self, request: CreateSecretRequest):
        table = self.get_secrets_table()
        secret_object = Secret(
            pk = "secret",
            sk =str(uuid.uuid4()),
            secret =  request.secret,
            expiry = (datetime.utcnow() + timedelta(seconds=request.ttl))
        )
        table.put_item(Item=json.loads(secret_object.json()))
        return secret_object
    
    def get_secret(self, token: str):
        table = self.get_secrets_table()
        response = table.get_item(
            Key={'pk':'secret','sk':token}
        )
        if "Item" not in response:
            return None 
        dynamo_response = Secret.parse_obj(response["Item"])
        table.delete_item(
            Key={
                "pk": f"secret",
                "sk": f"{token}",
            }
        )
        if dynamo_response.expiry < datetime.utcnow():
            return None
        return dynamo_response