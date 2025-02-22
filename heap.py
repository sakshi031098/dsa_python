class Heap:
    def __init__(self):
        self.heap = []

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index-1)//2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, element):
        if len(self.heap) == 0:
            self.heap.append(element)
            return True
        else:
            self.heap.append(element)
            current_idx = len(self.heap) - 1
            parent_index = self.get_parent_index(current_idx)
            parent_element = self.heap[parent_index]
            while parent_element < element and parent_index >=0:
                self.swap(current_idx, parent_index)
                current_idx = parent_index
                parent_index = self.get_parent_index(current_idx)
                parent_element = self.heap[parent_index]

            return True


    def remove(self):

        if len(self.heap) == 1:
            self.heap.pop()
        elif len(self.heap) == 0:
            return False
        else:
            self.heap[0] = self.heap.pop()
            self.sink_down(0)
        return True

    def sink_down(self, index):

        left_child = self.get_left_child_index(index)
        rigth_child = self.get_right_child_index(index)
        max_idx = 0
        while True:
            if self.heap[left_child] > self.heap[index] and left_child < len(self.heap):
                max_idx = left_child
            if self.heap[rigth_child] > self.heap[index] and rigth_child < len(self.heap):
                max_idx = rigth_child
            if max_idx != index:
                self.swap(index, max_idx)
                max_idx = index
            else:
                return


myheap = Heap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)

print(myheap.heap)


myheap.remove()

print(myheap.heap)


myheap.remove()

print(myheap.heap)