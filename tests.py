import unittest

import models


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


if __name__ == '__main__':
    unittest.main()
