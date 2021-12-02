import utils


def create_task(content):
    """a factory function used to create new tasks"""
    return {
        'id': utils.get_serial_id(),
        'content': content,
        'is_done': False
    }


if __name__ == '__main__':
    tasks_to_add = ['watch a movie', 'call mom', 'finish homework']
    tasks = [create_task(content) for content in tasks_to_add]
    print(tasks)
