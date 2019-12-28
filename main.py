# -*- conding: utf-8 -*-
#!./.venv/bin/python3
""" Welcome to LWS! For datails open file 'README.md' """

# Import modules
from sys import argv, stdout, stderr, path
from os import name, path, listdir, getcwd
from logging import getLogger, FileHandler, StreamHandler, DEBUG, INFO, WARNING, ERROR
from time import sleep, perf_counter, time

from colorama import Fore, Back

from server import ServerHTTP

def main():
    commands = ["run-server", "migrate"]
    for key in argv:
        if key.endswith(".py"):
            continue
        if key in commands:
            pass
        else:
            print("Command '"+key+"' not found. Input --help or -h or ?, for print more info")
            exit()

if __name__ == "__main__":
    if name != "posix":
        print("This app is not working on "+name)
        inp = input("Conntinue (y/n)")
        if inp == "y":
            pass
        else:
            print("Exit")
            exit()
    main()

