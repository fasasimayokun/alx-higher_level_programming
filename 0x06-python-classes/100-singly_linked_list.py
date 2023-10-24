#!/usr/bin/python3
"""a singly linked list class"""


class Node:
    """a node template for the linked list"""
    def __init__(self, data, next_node=None):
        """initializes the new node
        Args:
            data (int): the integer data of the new node
            next_node (Node): the next nod
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """the get data property of the new node"""
        return self.__data

    @data.setter
    def data(self, value):
        """the set data property and checks if the value is an int"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """the getter next_node property of the new node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """the setter property of the next_node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """the singly linked list template"""
    def __init__(self):
        """initializes the head node"""
        self.__head = None

    def sorted_insert(self, value):
        """it return the linked list in a sorted order
        Args:
            value (Node): the new node inserted
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr = self.__head
            while (curr.next_node is not None and
                    curr.next_node.data < value):
                curr = curr.next_node
            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """prints out the nodes in the linked list"""
        nodes = []
        curr = self.__head
        while curr is not None:
            nodes.append(str(curr.data))
            curr = curr.next_node
        return ("\n".join(nodes))
