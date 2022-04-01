import unittest

from task import *


class Test(unittest.TestCase):
    task_instance = Task()

    task_list = []

    def unittest_Add(self):
        for i in range(5):
            task_title = "TASK " + str(i)
            self.task_instance.Add(task_title)
            self.task_list.append(task_title)
            self.assertEqual(self.task_list, self.task_instance.list)
