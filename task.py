class Task:
    list = []

    p = """
Command Line Todo application
=============================

Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task
"""

    def __init__(self) -> None:
        pass

    def Add(self, title: str):
        self.list.append(title)

    def Remove(self, index: int):
        self.list.pop(index)

    def List(self):
        if len(self.list) == 0:
            print("\033[31m", "No todos for today! :)", "\x1b[0m")
            return
        for line in self.list:
            print(self.list)

    def Complete(self, index):
        pass

    def Load():
        pass

    def Save():
        pass
