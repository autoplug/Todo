#!/usr/bin/env python3
task_list = []
print('\033[31m' + 'Success!' + '\x1b[0m')


def welcome():
    p = """
$ todo

Command Line Todo application
=============================

Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task
    """
    print(p)


def Add_task(subject):
    task_list.append({"title": subject})


def Print_task():
    print(task_list)


while True:
    command = input()

    if command == "-a":
        Add_task(input())
    if command == "-l":
        Print_task()
