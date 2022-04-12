# For local evaluator
from ting_file_management.node import Node


class Queue:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        first_value = Node(value)
        first_value.next = self.head_value
        self.head_value = first_value
        self.__length += 1

    def dequeue(self):
        """Aqui irá sua implementação"""

    def search(self, index):
        """Aqui irá sua implementação"""
