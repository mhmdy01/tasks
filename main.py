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

    # inform user
    click.echo(f"""Added "{new_task['content']}" to your task list.""")

@click.option('-i', '--incomplete', 'status', flag_value='incomplete', default=True)
@click.option('-c', '--complete', 'status', flag_value='complete')
@click.option('-a', '--all', 'status', flag_value='all')
@cli.command()
def show(status):
    """Filter tasks by status. By default only shows `incomplete` tasks"""
    # read tasks
    tasks = storage.read_tasks_from_json()

    # @disply to user, we need to know 2 things: which tasks, which msg?
    # filter tasks by status
    # and generate msg based on #filtered_tasks
    if status == 'incomplete':
        # filtered_tasks = [t for t in tasks.values() if not t['is_done']]
        filtered_tasks = list(itertools.filterfalse(operator.itemgetter('is_done'), tasks.values()))
        msg = "You have the following incomplete tasks:"
        if not filtered_tasks:
            msg = "You don't have any tasks to do."
    elif status == 'complete':
        filtered_tasks = list(filter(operator.itemgetter('is_done'), tasks.values()))
        msg = "You have completed the following tasks:"
        if not filtered_tasks:
            msg = "You haven't completed any tasks yet."
    elif status == 'all':
        # we must cast tasks to dict_list here so it:
        # - matches the result of other filtering cases
        # - not break later while iterating over them (when informing user)
        filtered_tasks = list(tasks.values())
        msg = "You have the following tasks:"
        if not filtered_tasks:
            msg = "You didn't add any tasks yet."
    else:
        # is this block necessary?
        # cuz by default click should catch invalid arguments
        click.echo('Wrong option...')
        return

    # display filtered tasks
    click.echo(msg)
    for task in filtered_tasks:
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
