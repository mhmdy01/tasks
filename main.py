import click


@click.group()
def cli():
    """tasks is a CLI for managing your TODOs."""

@cli.command()
def add():
    """Add a new task to your TODO list"""
    click.echo('adding a new task...')

@cli.command()
def list():
    """List all of your incomplete tasks"""
    click.echo('listing incomplete tasks...')

@cli.command()
def do():
    """Mark a task on your TODO list as complete"""
    click.echo("completing a task...")

if __name__ == '__main__':
    cli()

