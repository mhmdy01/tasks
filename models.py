import utils


def create_task(content, tasks):
    """a factory function used to create new tasks"""
    return {
        'id': utils.get_serial_id(tasks),
        'content': content,
        'is_done': False
    }


if __name__ == '__main__':
    pass
