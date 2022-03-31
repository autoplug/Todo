#!/usr/bin/env python3
from task import *

task = Task()

while True:
    input_string = input("Enter command : ")

    command = input_string[0:3].strip()
    arg = input_string[3:].strip()

    if command == "-a":
        task.Add(arg)

    if command == "-l":
        task.Print()

    if command == "-r":
        task.Print()
        value = int(arg)
        task.Remove(value)

    if command == "-c":
        task.Print()
        value = int(arg)
        task.Complete(value)

    if command == "-q":
        break
