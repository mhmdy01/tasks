from rich.console import Console
from rich.table import Table


def display_tasks(msg, tasks):
    table = Table(title=msg)

    # add header
    # header = [
    #     # lable, style options
    #     ('ID', {'style': 'cyan'}),
    #     ('Task', {'style': 'magenta'}),
    #     ('Completed', {'style': 'green'}),
    # ]
    header = [
        # lable, style options
        ('ID', {'style': None}),
        ('Task', {'style': None}),
        ('Completed', {'style': None}),
    ]
    for col in header:
        table.add_column(col[0], **col[1])

    # add rows
    for task in tasks:
        table.add_row(*map(str, task.values()))

    # render the table and handle if empty
    console = Console()
    if table.rows:
        console.print(table)
    else:
        if msg.lower().startswith('all'):
            msg = 'Tasks'
        console.print(f"[i]There are no {msg}...[/i]")


if __name__ == '__main__':
    pass
