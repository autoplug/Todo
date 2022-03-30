import json


class Task:
    list = []

# print('\033[31m' + 'Success!' + '\x1b[0m')

    welcome = """
Command Line Todo application
=============================

Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task
"""

    def __init__(self):
        pass

    def Add(self, title: str):
        self.list.append({"title": title, "complete": False})

    def Remove(self, index: int):
        self.list.pop(index)

    def Print(self):
        if len(self.list) == 0:
            print("\033[31m", "No todos for today! :)", "\x1b[0m")
            return
        i = 0
        for line in self.list:
            i += 1
            if line['complete']:
                print("\033[37m", i, "[X]", line["title"], "\x1b[0m")
            else:
                print("\033[37m", i, "[ ]", line["title"], "\x1b[0m")

    def Complete(self, index: int):
        self.list[index]["complete"] = True

    def Load(self):
        try:
            f = open("db.json", "r")
            self.list = json.loads(f.read())
        except:
            print("can not load var")

    def Save(self):
        try:
            f = open("db.json", "w")
            f.write(json.dumps(self.list))
            f.close()
        except:
            print("Can not save.")
