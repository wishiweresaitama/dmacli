from pydantic import BaseModel, Field

class ConfigurationModel(BaseModel):
    originPath: str = Field(default='')
    gamePath: str = Field(default='')
    toolsPath: str = Field(default='')
    drivePath: str = Field(default='')
    buildPath: str = Field(default='')
    executeFile: str = Field(default='')
    serverExecuteFile: str = Field(default='')
    clientExecuteFile: str = Field(default='')
    logRetentionDays: int = Field(default=30)
    mods: list = Field(default=[])
    clientProfile: str = Field(default='')
    serverProfile: str = Field(default='')
    serverMods: list = Field(default=[])
    serverArgs: list = Field(default=[])
    clientArgs: list = Field(default=[])

    @staticmethod
    def is_valid_parameter(param: str):
        return param in ConfigurationModel.__fields__
