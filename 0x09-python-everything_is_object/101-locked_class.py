#!/usr/bin/python3
'''a locked class template'''


class LockedClass:
    '''
    a class that prevent the usser from instantiating new locked class attr
    for anything except attrs called first_name
    '''
    __slots__ = ['first_name']
