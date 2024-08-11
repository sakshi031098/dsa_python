class Node:
    def __init__(self, *, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, *, value):
        self.node = Node(value=value)
        self.head = self.node
        self.tail = self.node
        self.length = 1

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.value, sep=',')
            node = node.next

    def append(self, *, value):
        last_node = Node(value=value)
        self.tail.next = last_node
        self.tail = last_node
        self.length = self.length + 1

    def prepend(self, *, value):
        first_node = Node(value=value)
        first_node.next = self.head
        self.head = first_node
        self.length = self.length + 1

    def pop_first_node(self):
        second_node = self.head.next
        self.head = second_node
        self.length = self.length - 1

    def insert_node(self, *, idx, value):
        if idx == 1:
            self.prepend(value=value)
        elif idx == self.length - 1:
            self.append(value=value)
        elif idx <= self.length:
            temp_node = self.head
            new_node = Node(value=value)
            for i in range(1, idx-1):
                temp_node = temp_node.next
            after_node = temp_node.next
            temp_node.next = new_node
            new_node.next = after_node
        else:
            print(f"could not insert node at {idx} as length of node is {self.length}")




l1 = LinkedList(value=4)

l1.append(value=5)
l1.append(value=10)
l1.prepend(value=2)
# l1.pop_first_node()
l1.insert_node(idx=2, value=500)
l1.print_list()
