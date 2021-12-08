import utils
import storage


def create_task(content, tasks):
    """a factory function used to create new tasks"""
    return {
        'id': utils.get_serial_id(tasks),
        'content': content,
        'is_done': False
    }


if __name__ == '__main__':
    tasks_to_add = ['watch a movie', 'call mom', 'finish homework']
    tasks = [create_task(content) for content in tasks_to_add]
    print(tasks)
