from abc import ABC, abstractmethod

from secret_sharing_api.models.secret import CreateSecretRequest

class DataService(ABC):
    @abstractmethod
    def add_secret(self, request: CreateSecretRequest):
        pass

    @abstractmethod
    def get_secret(self, token: str):
        pass