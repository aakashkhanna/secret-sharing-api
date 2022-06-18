from datetime import datetime
from pydantic import BaseModel

class CreateSecretRequest(BaseModel):
    secret: str
    ttl: int

class CreateSecretResponse(BaseModel):
    secret_identifier: str
    expiry: datetime