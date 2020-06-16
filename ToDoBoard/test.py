#!/usr/bin/env python3
import urwid, sys


def Read_ToDolsit():
    TODO = open(sys.path[0]+"/ToDolist",'r').read().split('\n')[:-1]
    Result = []
    for i in TODO:
        Result += [i.split()]
    return Result

print(Read_ToDolsit())
