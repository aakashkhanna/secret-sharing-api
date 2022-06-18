from pydantic import BaseModel

class Config(BaseModel):
    aws_endpoint_url: str
    aws_region_name: str
    aws_dynamo_name: str
    aws_access_key_id: str
    aws_secret_access_key: str