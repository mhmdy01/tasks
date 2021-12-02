import operator
import itertools

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
    # create a new task
    new_task = models.create_task(' '.join(content))

    # save it to json file
    tasks = storage.read_tasks_from_json()
    tasks[new_task['id']] = new_task
    storage.write_tasks_to_json(tasks)

    # alert user
    click.echo(f"""Added "{new_task['content']}" to your task list.""")

@cli.command()
def list():
    """List all of your incomplete tasks"""
    # read tasks and filter them by status
    tasks = storage.read_tasks_from_json()
    # incomplete_tasks = [t for t in tasks.values() if not t['is_done']]
    incomplete_tasks = itertools.filterfalse(operator.itemgetter('is_done'), tasks.values())

    # display filtered tasks
    click.echo("You have the following tasks:")
    for task in incomplete_tasks:
        click.echo(f"{task['id']}. {task['content']}")

@cli.command()
@click.argument('task_id')
def do(task_id):
    """Mark a task on your TODO list as complete"""
    # read task and handle if not found
    tasks = storage.read_tasks_from_json()
    try:
        task = tasks[task_id]
    except KeyError:
        click.echo(f"There is no task with id {task_id}")
        return

    # update and save
    task['is_done'] = True
    storage.write_tasks_to_json(tasks)

    # inform user
    click.echo(f"""You have completed the "{task['content']}" task.""")


if __name__ == '__main__':
    cli()
