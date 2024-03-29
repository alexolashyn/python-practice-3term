from node import Node
from helpers import numeric_input
import random as rnd


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        node = self.head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def __getitem__(self, index):
        position = 0
        node = self.head
        if index >= self.__len__() or index < 0:
            print('There is no such position in linked list!')
            return
        while position != index:
            node = node.next
            position += 1
        return node

    def __setitem__(self, index, value):
        position = 0
        node = self.head
        if index >= self.__len__() or index < 0:
            print('There is no such position in linked list!')
            return
        while position != index:
            node = node.next
            position += 1
        node.value = value

    def __str__(self):
        output = '['
        node = self.head
        if node:
            output += str(node.value)
            node = node.next
            while node:
                output += ', ' + str(node.value)
                node = node.next
        output += ']'
        return output

    def is_empty(self):
        return self.head == None

    def append(self, value):
        node = self.head
        if not (self.is_empty()):
            while node.next:
                node = node.next
            node.next = Node(value)
        else:
            self.head = Node(value)

    def input(self, length):
        while length:
            self.append(numeric_input())
            length -= 1

    def generate(self, length, a, b):
        while length:
            value = rnd.randint(a, b)
            self.append(value)
            length -= 1

    def check_negative(self):
        node = self.head
        while node.next:
            if node.value > 0:
                return False
            node = node.next
        return True

    def find_maximum(self):
        if not self.is_empty():
            node = self.head
            maximum = node.value
            while node.next:
                node = node.next
                if node.value > maximum:
                    maximum = node.value
            return maximum
        else:
            return

    def find_position(self, value):
        if not self.is_empty():
            position = 0
            node = self.head
            while node.value != value:
                position += 1
                node = node.next
            return position
        else:
            return

    def cube_of_value(self):
        if not self.is_empty():
            maximum = self.find_maximum()
            node = self.head
            while node.value != maximum:
                node.value = node.value ** 3
                node = node.next
        else:
            return

    def insert(self, value, position):
        if position < 0:
            print('There is no such position in linked list!')
            return
        if position >= self.__len__():
            self.append(value)
        if position == 0:
            self.head = Node(value, self.head)
        else:
            i = 0
            node = self.head
            while node.next:
                if i == position - 1:
                    node.next = Node(value, node.next)
                node = node.next
                i += 1

    def remove(self, position):
        if self.head is None:
            return
        index = 0
        node = self.head
        while node.next and index < position:
            previous_node = node
            node = node.next
            index += 1
        if index == 0:
            self.head = self.head.next
        else:
            previous_node.next = node.next

    def clear(self):
        node = self.head
        if self.is_empty():
            print('Linked list is already empty!')
            return
        while node:
            self.head = node.next
            node = self.head
