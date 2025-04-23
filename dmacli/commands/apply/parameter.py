import click
from dmacli.models.config import ConfigurationModel
from dmacli.configuration import Configuration

@click.command(name='parameter')
@click.argument('param', type=str, required=True)
@click.argument('value', type=str, required=True)
def parameter(param: str, value: str):
    if not ConfigurationModel.is_valid_parameter(param):
        print(f"Parameter {param} is not valid")
        return
    
    Configuration().set(param, value)
    Configuration().save()

    print("Configuration updated successfully")
    print(f"Parameter {param} set to {value}")
