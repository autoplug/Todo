import json


class Task:
    list = []

    def __init__(self):
        self.Load()

    def Add(self, title: str):
        title = title.strip()
        if not title:
            return
        self.list.append({"title": title, "complete": 0})
        print("\u001b[32m", "Successfully add task to list.", "\u001b[0m")
        self.Save()
        return

    def Remove(self, index: int):
        if index > len(self.list):
            print("\033[31m", "There is not task with this number.", "\u001b[0m")
            return

        self.list.pop(index)
        print("\033[31m", "Successfully remove task from list.", "\u001b[0m")
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
        if index > len(self.list):
            print("There is not task with this number.")
            return

        self.list[index]["complete"] = 0 if self.list[index]["complete"] else 1
        print("\u001b[33m", "Successfully complete task.", "\x1b[0m")
        self.Save()

    def Load(self):
        try:
            f = open("db.json", "r")
            self.list = json.loads(f.read())
            f.close()
        except:
            print("Can not load file.")

    def Save(self):
        try:
            f = open("db.json", "w")
            f.write(json.dumps(self.list))
            f.close()
        except:
            print("Can not save.")
