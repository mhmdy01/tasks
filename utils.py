import random


def get_random_id():
    """generate random ids for new tasks."""
    # must use a wide range to avoid values collision
    return random.randint(1, 1_000_000)

def get_serial_id(tasks):
    """generate sequential ids for new tasks."""
    # a sequential id is calculated through incrementing current max id
    # so we need to find max_id first by scanning through old tasks
    # `int` is used to cast ids to integers, as json keys -by default- are strings
    # `default` is used to handle when there are no tasks yet
    max_id = max(map(int, tasks), default=0)
    return max_id + 1
