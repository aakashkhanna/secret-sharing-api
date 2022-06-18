from dotjson import model_dotjson
from secret_sharing_api.models.configs import Config

def get_configs():
    configs:Config = model_dotjson(Config, json_path="settings.local.json")
    return configs