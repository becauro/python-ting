class Node:
    def __init__(self, value):
        self.value = value  # ๐ฒ Dado a ser armazenado
        self.next = None  # ๐ Forma de apontar para outro nรณ

    def __str__(self):
        # return (self.value, self.next)
        return f"Node(value={self.value}, next={self.next})"
