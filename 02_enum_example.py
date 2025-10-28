from enum import Enum
from fastapi import FastAPI

api = FastAPI()

class ModelName(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

@api.get("/model/{model_name}")
def model_name(model_name: ModelName):
    if model_name is ModelName.SMALL:
        return {"Model Name": model_name, "Message": "You like small :)"}
    elif model_name is ModelName.MEDIUM:
        return {"Model Name": model_name, "Message": "You like medium :)"}
    elif model_name is ModelName.LARGE:
        return {"Model Name": model_name, "Message": "You like large :)"}

@api.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}