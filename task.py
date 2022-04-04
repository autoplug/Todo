import json


class Task:
    list = []
    path = ""

    # initialize class
    def __init__(self, path: str = "db.json"):
        self.path = path
        self.Load()

    # Add task to the list
    def Add(self, title: str):
        title = title.strip()
        if not title:
            print("\033[31m", "Unable to add: no task provided", "\u001b[0m")
            return
        self.list.append({"title": title, "complete": 0})
        print("\u001b[32m", "Successfully add task to list.", "\u001b[0m")
        self.Save()
        return

    # remove task from list
    def Remove(self, index: int):
        if index > len(self.list):
            print("\033[31m",
                  "Unable to remove: index is out of bound.", "\u001b[0m")
            return

        self.list.pop(index)
        print("\033[31m", "Successfully remove task from list.", "\u001b[0m")
        self.Save()

    # print all task in command line
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

    # mark task as complete
    def Complete(self, index: int):
        if index > len(self.list):
            print("\033[31m", "There is not task with this number.", "\x1b[0m")
            return

        self.list[index]["complete"] = 0 if self.list[index]["complete"] else 1
        print("\u001b[33m", "Successfully complete task.", "\x1b[0m")
        self.Save()

    # load saved tasks
    def Load(self):
        try:
            f = open(self.path, "r")
            self.list = json.loads(f.read())
            f.close()
        except:
            print("Can not load file.")

    # save the task
    def Save(self):
        try:
            f = open(self.path, "w")
            f.write(json.dumps(self.list))
            f.close()
        except:
            print("Can not save.")
