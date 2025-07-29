from datetime import datetime
from pydantic import BaseModel

class Secret(BaseModel):
    pk: str
    sk: str
    secret: str
    expiry: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

        json_decoders = {
            datetime: lambda v: datetime.fromisoformat(v)
        }