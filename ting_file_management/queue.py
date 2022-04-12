# For local evaluator
from ting_file_management.node import Node


class Queue:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def __str__(self):
        return f"Queue(len={self.__length}, value={self.head_value})"

    def enqueue(self, value):
        # This func insert value in the end of queue
        last_value = Node(value)
        current_value = self.head_value

        # If queue is empty, the value is inserted directly into its head
        if self.__len__() == 0:
            new_value = Node(value)
            new_value.next = self.head_value
            self.head_value = new_value
            self.__length += 1

            return self.head_value

        while current_value.next:
            current_value = current_value.next
        current_value.next = last_value
        self.__length += 1

    def dequeue(self):
        value_to_be_removed = self.head_value
        if value_to_be_removed:
            self.head_value = self.head_value.next
            value_to_be_removed.next = None
            self.__length -= 1
        return value_to_be_removed.value

    def search(self, index):
        value_returned = None
        value_to_be_returned = self.head_value
        if value_to_be_returned:
            if 0 <= index <= self.__len__():
                while index > 0 and value_to_be_returned.next:
                    value_to_be_returned = value_to_be_returned.next
                    index -= 1
            else:
                raise IndexError("invalid index")

            if value_to_be_returned:
                value_returned = value_to_be_returned.value
        else:
            raise IndexError("Thre is no node in the queue")

        return value_returned
