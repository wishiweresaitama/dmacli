from pydantic import BaseModel

class ConfigurationModel(BaseModel):
    originPath: str
    gamePath: str
    toolsPath: str
    drivePath: str
    buildPath: str
    executeFile: str
    serverExecuteFile: str
    clientExecuteFile: str
    logRetentionDays: int
    mods: list
    clientProfile: str
    serverProfile: str
    serverMods: list
    serverArgs: list
    clientArgs: list
