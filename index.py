#!/usr/bin/env python3
from task import *

task = Task()

task.Load()

while True:
    command = input("Enter command : ")

    if command == "-a":
        value = input("Enter your task : ")
        task.Add(value)
        task.Save()
    if command == "-l":
        task.Print()
    if command == "-r":
        task.Print()
        value = int(input())
        task.Remove(value)
    if command == "-c":
        task.Print()
        value = int(input("Complete : "))
        task.Complete(value)
    if command == "-q":
        break
