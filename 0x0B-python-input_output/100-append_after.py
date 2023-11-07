#!/usr/bin/python3
"""an append after func module"""


def append_after(filename="", search_string="", new_string=""):
    """a func that appends a new str after a line containig
    the search string in the filename"""
    with open(filename, 'r', encoding='utf-8') as fle:
        list_line = []
        while 1:
            ln = fle.readline()
            if ln == '':
                break
            list_line.append(ln)
            if search_string in ln:
                list_line.append(new_string)
    with open(filename, 'w', encoding='utf-8') as fle:
        fle.writelines(list_line)
