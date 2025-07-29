from dotjson import load_dotjson, model_dotjson
from secret_sharing_api.models.configs import DynamoConfig, RedisConfig

load_dotjson("settings.local.json")

class ConfigService:
    @staticmethod
    def get_dynamo_configs():
        configs:DynamoConfig = DynamoConfig()
        return configs

    @staticmethod
    def get_redis_configs():
        configs: RedisConfig = RedisConfig()
        return configs