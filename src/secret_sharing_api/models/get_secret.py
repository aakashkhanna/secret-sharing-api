from pydantic import BaseModel

class GetSecretResponse(BaseModel):
    secret: str

