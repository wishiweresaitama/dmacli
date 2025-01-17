import click


@click.command()
@click.option("--name", prompt="Your name", help="The person to greet.")
def cli(name: str):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    cli()