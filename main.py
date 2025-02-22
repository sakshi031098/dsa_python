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
        pop_node = self.head
        self.head = self.head.next
        self.length = self.length - 1
        return pop_node

    def insert_node(self, *, idx, value):
        if idx > self.length or idx not in range(1, self.length+1):
            return
        if idx == 1:
            self.prepend(value=value)
        elif idx == self.length - 1:
            self.append(value=value)
        elif idx <= self.length:
            new_node = Node(value=value)
            temp_node = self.get_value_by_index(index=idx-1)
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length = self.length + 1
        else:
            print(f"could not insert node at {idx} as length of node is {self.length}")

    def del_linkedList(self):
        if self.length == 0:
            self.head = None
            self.tail = None

    def pop(self, *, index=None):
        if self.head.next is not None:
            if index == 1:
                temp_node = self.pop_first_node()
            elif index == self.length:
                temp_node = self.pop()
            elif index is None:
                temp_node = self.head
                while temp_node.next is not None:
                    pre_node = temp_node
                    temp_node = temp_node.next
                self.tail = pre_node
                self.tail.next = None
            elif index > self.length:
                print("Index is greater than length of LL")
                return
            elif index == 0:
                print("Index does not starts from zero")
                return
            else:
                pre_node = self.get_value_by_index(index=index-1)
                temp_node = self.get_value_by_index(index=index)
                pre_node.next = temp_node.next
                temp_node.next = None
        else:
            print("Linked List is empty")
        self.length = self.length - 1
        self.del_linkedList()
        return temp_node.value
    def reverse(self):
        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node
        before = None
        for _ in range(self.length):
            after = temp_node.next
            temp_node.next = before
            before = temp_node
            temp_node = after


    def get_value_by_index(self, *, index):
        if index > self.length or index not in range(1, self.length+1):
            return
        temp_node = self.head
        for idx in range(1, index):
            temp_node = temp_node.next
        return temp_node

    def set_value(self, idx, value):
        temp_node = self.get_value_by_index(index=idx)
        if temp_node:
            temp_node.value = value
            return True
        return False

l1 = LinkedList(value=4)
l1.prepend(value=2)
print("length", l1.length)

# l1.pop_first_node()
l1.insert_node(idx=2, value=500)

l1.print_list()

print("after pop ..........")

# print(l1.pop(index=3))
# print("result is ")
# l1.print_list()
print("length", l1.length)
l1.reverse()
l1.print_list()


# print("### get value")
# print(l1.get_value_by_index(index=0))

# l1.set_value(3, 100)
# print("new list  is ")
# l1.print_list()
