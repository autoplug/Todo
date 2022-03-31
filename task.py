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
    -q   Quit the app.
"""

    def __init__(self):
        print(self.welcome)
        self.Load()

    def Add(self, title: str):
        self.list.append({"title": title, "complete": 0})
        self.Save()

    def Remove(self, index: int):
        index -= 1
        self.list.pop(index)
        self.Save()

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
        index -= 1
        self.list[index]["complete"] = 0 if self.list[index]["complete"] else 1
        self.Save()

    def Load(self):
        try:
            f = open("db.json", "r")
            self.list = json.loads(f.read())
            f.close()
        except:
            print("can not load var")

    def Save(self):
        try:
            f = open("db.json", "w")
            f.write(json.dumps(self.list))
            f.close()
        except:
            print("Can not save.")
