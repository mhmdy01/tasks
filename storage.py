import json
from pathlib import Path


JSON_FILE_PATH = Path.home() / 'tasks.json'

def read_tasks_from_json(file_path=JSON_FILE_PATH):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            contents = json.load(f)
    except FileNotFoundError:
        return {}
    # TODO
    # add exception handler for json errors
    # but question is: what to do in such case?
    # delete the file?
    # only delete file contents and return empty dict?
    # eg. write_to_json({})
    else:
        return contents

def write_tasks_to_json(tasks, file_path=JSON_FILE_PATH):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2)


if __name__ == '__main__':
    tasks = read_tasks_from_json()
    print(json.dumps(tasks, indent=2))
