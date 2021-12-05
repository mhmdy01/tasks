import utils
import storage


def create_task(content):
    """a factory function used to create new tasks"""
    # read stored tasks
    tasks = storage.read_tasks_from_json()

    # create a new task
    task = {
        'id': utils.get_serial_id(tasks),
        'content': content,
        'is_done': False
    }

    # add it to stored tasks then save back to json file
    tasks[task['id']] = task
    storage.write_tasks_to_json(tasks)

    # send it to command handler
    return task


if __name__ == '__main__':
    tasks_to_add = ['watch a movie', 'call mom', 'finish homework']
    tasks = [create_task(content) for content in tasks_to_add]
    print(tasks)
