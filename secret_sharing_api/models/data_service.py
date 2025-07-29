from pydantic import BaseModel

class DataServiceCreateResponse(BaseModel):
    token: str
    ttl: int

class DataServiceRetrieveResponse(BaseModel):
    secret: str