class Node:
    def __init__(self, value):
        self.value = value  # 🎲 Dado a ser armazenado
        self.next = None  # 👉 Forma de apontar para outro nó

    def __str__(self):
        # return (self.value, self.next)
        return f"Node(value={self.value}, next={self.next})"
