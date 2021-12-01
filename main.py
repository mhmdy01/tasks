import click

import models


@click.group()
def cli():
    """tasks is a CLI for managing your TODOs."""

@cli.command()
@click.argument('content', nargs=-1, required=True)
def add(content):
    """Add a new task to your TODO list"""
    task = models.create_task(' '.join(content))
    click.echo(f"""Added "{task['content']}" to your task list.""")

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

