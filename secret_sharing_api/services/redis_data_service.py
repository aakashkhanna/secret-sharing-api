import redis
import uuid
import json
from datetime import timedelta

from secret_sharing_api.models.configs import RedisConfig
from secret_sharing_api.models.secret import CreateSecretRequest
from secret_sharing_api.models.data_service import DataServiceCreateResponse, DataServiceRetrieveResponse
from secret_sharing_api.services.data_service import DataService


class RedisDataService(DataService):
    def __init__(self, config: RedisConfig):
        self.client = r = redis.Redis(
                host=config.redis_host,
                port=int(config.redis_port),
                password=config.redis_secret,
                ssl=True
            )

    def add_secret(self, request: CreateSecretRequest) -> DataServiceCreateResponse:
        token = str(uuid.uuid4())
        secret_data = {
            "secret": request.secret
        }

        self.client.setex(token, timedelta(seconds=request.ttl), json.dumps(secret_data))
        return DataServiceCreateResponse(ttl=request.ttl, token=token)

    def get_secret(self, token: str) -> DataServiceRetrieveResponse:
        secret_json = self.client.get(token)
        secret = json.loads(secret_json)
        if secret_json is None:
            return None
        self.client.delete(token)
        return DataServiceRetrieveResponse(secret=secret.get("secret"))
