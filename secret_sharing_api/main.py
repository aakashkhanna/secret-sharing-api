from secret_sharing_api.services.config_service import ConfigService
from secret_sharing_api.services.dynamo_data_service import DynamoDataService
from secret_sharing_api.models.secret import GetSecretResponse
from secret_sharing_api.models.secret import CreateSecretRequest, CreateSecretResponse
from fastapi import FastAPI, HTTPException
from secret_sharing_api.services.redis_data_service import RedisDataService
app = FastAPI()


@app.post("/post-secret/")
def add_secret(request: CreateSecretRequest):
    try:
        data_service = RedisDataService(ConfigService.get_redis_configs())
        data_service_response = data_service.add_secret(request=request)
        response = CreateSecretResponse(secret_identifier=data_service_response.token, ttl=data_service_response.ttl)
        return response
    except Exception as e:
        raise e

@app.get("/get-secret/{token}")
def read_secret(token: str):
    try:
        data_service = RedisDataService(ConfigService.get_redis_configs())
        data_service_response = data_service.get_secret(token=token)
        if data_service_response is None:
            raise HTTPException(404)
        else:
            response = GetSecretResponse(secret=data_service_response.secret)
            return response
    except Exception as e:
        raise e