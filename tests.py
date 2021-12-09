import unittest
import json
from pathlib import Path

import models
import storage


class CreateTaskTests(unittest.TestCase):
    """tests for models.create_task"""
    def test_create_task_return_type(self):
        """should return a dict"""
        task = models.create_task("task #1", {})
        self.assertIsInstance(task, dict)

    def test_create_task_id(self):
        """should return a dict with id:1"""
        task = models.create_task("task #1", {})
        self.assertEqual(task['id'], 1)

    def test_create_task_isdone(self):
        """should return a dict with is_done:false"""
        task = models.create_task("task #1", {})
        self.assertFalse(task['is_done'])

    def test_create_task_content(self):
        """should return a dict with content field"""
        tasks_to_add = ['watch a movie', 'call mom', 'finish homework']
        for content in tasks_to_add:
            task = models.create_task(content, {})
            self.assertEqual(task['content'], content)


class ReadTasksFromJsonTests(unittest.TestCase):
    """tests for storage.read_tasks_from_json"""
    def setUp(self):
        """init some data and write them to test file"""
        # init paths
        self.file_that_doesnt_exist = Path.cwd() / 'wrong_file.json'
        self.file_that_exists = Path.cwd() / 'delete_me.json'

        # init tasks
        self.tasks = {
            '1': {
                'id': 1,
                'content': 'task #1',
                'is_done': False
            }
        }

        # init files
        with open(self.file_that_exists, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f)

    def test_read_tasks_file_doesnt_exist(self):
        """should return an empty dict if json file doesn't exist"""
        tasks = storage.read_tasks_from_json(self.file_that_doesnt_exist)
        self.assertIsInstance(tasks, dict)
        self.assertEqual(tasks, {})

    def test_read_tasks_file_exists(self):
        """should return file contents as dict if json file exists"""
        tasks = storage.read_tasks_from_json(self.file_that_exists)
        self.assertIsInstance(tasks, dict)
        self.assertEqual(tasks, self.tasks)

    def tearDown(self):
        """delete test file"""
        self.file_that_exists.unlink()


if __name__ == '__main__':
    unittest.main()
