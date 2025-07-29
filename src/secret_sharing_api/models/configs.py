from pydantic import BaseSettings

class Config(BaseSettings):
    pass

class DynamoConfig(Config):
    aws_endpoint_url: str
    aws_region_name: str
    aws_dynamo_name: str
    aws_access_key_id: str
    aws_secret_access_key: str

class RedisConfig(Config):
    redis_host: str
    redis_port: str
    redis_secret: str
    