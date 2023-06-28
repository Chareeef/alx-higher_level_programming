#!/usr/bin/python3
''' Implement Singly Linked List in Python using Classes '''


class Node:
    ''' A Singly Linked List node
    Initialized with private attributes "data" and "next_node" '''
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        elif type(next_node) is not Node and next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__data = data
            self.__next_node = next_node

    @property
    def data(self):
        '''Getter and Setter of the sll data'''
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        '''Getter and Setter of the next_node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, next_n):
        if type(next_n) is not Node and next_n is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_n

class SinglyLinkedList:
    '''A Singly Linked List class with head as private attribute
    and sorted_insert() method'''

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        '''Inserts a new Node into the correct sorted
        position in the list (increasing order)'''

        current_n = self.__head
        if current_n is None:
            self.__head = Node(value)
            return

        next_n = current_n.next_node
        if next_n is None or value < current_n.data:
            if value < current_n.data:
                self.__head = Node(value, current_n)
            else:
                current_n.next_node = Node(value)
            return

        while current_n.next_node is not None:
            if value > next_n.data:
                current_n = current_n.next_node
                next_n = current_n.next_node
            else:
                break

        new = Node(value, next_n)

        if current_n is self.__head:
            self.__head = new
        elif current_n is not None:
            current_n.next_node = new

    def __str__(self):
        '''The readable representation of SinglyLinkedList'''
        representation = ''
        current_n = self.__head
        while current_n is not None:
            representation += str(current_n.data)
            if current_n.next_node is not None:
                representation += '\n'
            current_n = current_n.next_node

        return representation
