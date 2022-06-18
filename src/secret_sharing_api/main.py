from secret_sharing_api.services.dynamo_data_service import DynamoDataService
from secret_sharing_api.models.get_secret import GetSecretResponse
from secret_sharing_api.models.create_secret import CreateSecretRequest, CreateSecretResponse
from fastapi import FastAPI, HTTPException
app = FastAPI()

dynamo = DynamoDataService()

@app.post("/post-secret/")
def add_secret(request: CreateSecretRequest):
    try:
        dynamo_response = dynamo.add_secret(request=request)
        response = CreateSecretResponse(secret_identifier=dynamo_response.sk, expiry=dynamo_response.expiry)
        return response
    except Exception as e:
        raise e

@app.get("/get-secret/{token}")
def read_secret(token: str):
    try:
        dynamo_response = dynamo.get_secret(token=token)
        if dynamo_response is None:
            raise HTTPException(404)
        else:
            response = GetSecretResponse(secret=dynamo_response.secret)
            return response
    except Exception as e:
        raise e