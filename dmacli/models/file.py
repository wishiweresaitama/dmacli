from pydantic import BaseModel

class FileModel(BaseModel):
    name: str
    context: str
