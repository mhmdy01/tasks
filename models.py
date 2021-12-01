import random

import storage


def get_random_id():
    """generate random ids for new tasks."""
    # must use a wide range to avoid values collision
    return random.randint(1, 1_000_000)

def get_serial_id():
    """generate sequential ids for new tasks."""
    # a sequential id is calculated through incrementing current max id
    # so we need to find max_id first by scanning through old tasks
    tasks = storage.read_tasks_from_json()
    # `int` is used to cast ids to integers, as json keys -by default- are strings
    # `default` is used to handle when there are no tasks yet
    max_id = max(map(int, tasks), default=0)
    return max_id + 1

def create_task(content):
    """a factory function used to create new tasks"""
    return {
        'id': get_serial_id(),
        'content': content
    }


if __name__ == '__main__':
    tasks_to_add = ['watch a movie', 'call mom', 'finish homework']
    tasks = [create_task(content) for content in tasks_to_add]
    print(tasks)
