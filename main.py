import click

import models
import storage


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
    tasks = storage.read_tasks_from_json()

    click.echo("You have the following tasks:")
    for task_id, task in tasks.items():
        click.echo(f"{task['id']}. {task['content']}")

@cli.command()
def do():
    """Mark a task on your TODO list as complete"""
    click.echo("completing a task...")

if __name__ == '__main__':
    cli()

