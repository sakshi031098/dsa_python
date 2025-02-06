class Node:
    def __init__(self,value):
        self.next = None
        self.value = value
    
class LinkedList:
    def __init__(self,value):
        self.node=Node(value)
        self.head = self.node
        self.tail = self.node
        self.length = 1
        

    def append_at_start(self, value):
        node = Node(value)
        self.length +=1
        node.next = self.head
        self.head = node

    def remove_at_start(self):
        self.length-=1
        if self.length == 0:
             self.tail = None
             self.head = None
        else:
            temp = self.head.next 
            self.head.next = None
            self.head = temp

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node

        else:
            temp = self.tail
            temp.next = node
            self.tail = node
        self.length += 1

    def remove_last(self):
        temp = self.head
        while temp.next and temp.next != self.tail:
            temp = temp.next
        removed_ele = temp.next.value
        temp.next = None
        self.tail = temp
        self.length-=1
        return removed_ele

    def print_linked_list(self):
            temp = self.head
            while temp is not None:
                 print(temp.value)
                 temp = temp.next
                 
    def append_at_index(self, value, index):
        if index == 0:
            self.append_at_start(value)
        elif index == self.length:
            self.append(value)
        else:
            prev_value = self.head
            counter = 0
            node = Node(value)
            while counter<index-1 and self.length>index:
                counter+=1
                prev_value = prev_value.next
            node.next = prev_value.next
            prev_value.next = node
        self.length +=1


l =LinkedList(4)  
l.append_at_start(5)
l.append(6)
l.print_linked_list()
l.append_at_index(9,1)
print("print list")
l.print_linked_list()


        