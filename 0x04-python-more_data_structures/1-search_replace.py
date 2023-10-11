#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """a func that replaces all occurrences of an element by another in a new list."""
    new_list = []
    for num in range(len(my_list)):
        if search == my_list[num]:
            new_list.append(replace)
        else:
            new_list.append(my_list[num])
    return (new_list)
