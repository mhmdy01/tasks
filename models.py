from collections import namedtuple


Task = namedtuple('Task', ('id', 'content'))


if __name__ == '__main__':
    tasks_to_add = ['watch a movie', 'call mom', 'finish homework']
    tasks = [Task(i, content) for i, content in enumerate(tasks_to_add, start=1)]
    print(tasks)
