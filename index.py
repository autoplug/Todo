#!/usr/bin/env python3
from task import *

task = Task()

# print('\033[31m' + 'Success!' + '\x1b[0m')

while True:
    command = input()

    if command == "-a":
        task.Add(input())
    if command == "-l":
        task.List()
    if command == "-r":
        task.Remove(input())
    if command == "-c":
        task.Complete(input())
