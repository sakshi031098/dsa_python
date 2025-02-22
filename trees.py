class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            temp = self.root
            while temp is not None:
                if value < temp.value:
                    if temp.left is None:
                        temp.left = Node(value)
                    temp = temp.left
                elif value > temp.value:
                    if temp.right is None:
                        temp.right = Node(value)
                    temp = temp.right
                else:
                    return False
        return True

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return False



b = BinarySearchTree()
print(b.root)
b.insert(5)
b.insert(4)
b.insert(3)
b.insert(7)
b.insert(1)
b.insert(2)
b.insert(6)
print(b.contains(9))
# print(b1.root.value)
# print(b1.root.right.value)
# print(b1.root.left.value)
# print(b1.root.left.left.value)
# print(b1.root.right.left.value)
# print(b1.root.right.left.right.value)
