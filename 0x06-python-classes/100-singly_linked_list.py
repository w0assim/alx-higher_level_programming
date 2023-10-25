#!/usr/bin/python3
"""s"""

class Node:
    """s"""
    def __init__(self, data, next_node=None):
        """s"""
        self.data = data
        self.next_node = next_node


    @property
    def data(self):
        """s"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """s"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """s"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """s"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    class SinglyLinkedList:
        """s"""
        def __init__(self):
            """s"""
            self.__head = None

        def sorted_insert(self, value):
            """s"""
            new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

        def __str__(self):
            """s"""
            values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
