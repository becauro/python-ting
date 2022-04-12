# For local evaluator
from ting_file_management.node import Node

# For manual test local
# from node import Node


class Queue:
    def __init__(self):
        self.head_value = None
        self.__length = 0
        self.queue = set()
        self.files_stats = []  # Here

    def __len__(self):
        return self.__length

    def __str__(self):
        return f"Queue(len={self.__length}, value={self.head_value})"

    def enqueue(self, value):
        # This func insert value in the end of queue
        last_value = Node(value)
        exist = self.already_exist(value, len(list(self.queue)))

        if not exist:
            current_value = self.head_value

            # If queue is empty, the value is inserted directly into its head
            if self.__len__() == 0:
                new_value = Node(value)
                new_value.next = self.head_value
                self.head_value = new_value
                self.__length += 1

                # return self.head_value
                return

            while current_value.next:
                current_value = current_value.next
            current_value.next = last_value
            self.__length += 1

    def already_exist(self, value, length):
        # This func is called by enqueue()
        # This func help to throw out duplicate nodes

        print(self.queue)
        self.queue.add(value)
        if len(list(self.queue)) > length:
            print("New item")
            return False
        else:
            print("Item already exist")
            return True

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

        if value_to_be_returned and 0 <= index <= self.__len__():
            while index > 0 and value_to_be_returned.next:
                value_to_be_returned = value_to_be_returned.next
                index -= 1

            if value_to_be_returned:
                value_returned = value_to_be_returned.value
        else:
            raise IndexError("There is no node in the queue")

        return value_returned

    def set_files_stats(self, file_stat):
        self.files_stats.append(file_stat)
