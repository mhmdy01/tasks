import random


def get_random_id():
    """generate a random id for new tasks.
    must use a wide range to avoid values collision
    """
    return random.randint(1, 1_000_000)

def create_task(content):
    """a factory function used to create new tasks"""
    return {
        'id': get_random_id(),
        'content': content
    }


if __name__ == '__main__':
    tasks_to_add = ['watch a movie', 'call mom', 'finish homework']
    tasks = [create_task(content) for content in tasks_to_add]
    print(tasks)
