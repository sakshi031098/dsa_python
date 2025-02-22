class MinHeap:
    def __init__(self):
        self.heap = []

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, element):
        if len(self.heap) == 0:
            self.heap.append(element)
            return True
        else:
            self.heap.append(element)
            current_idx = len(self.heap)-1
            parent_idx = self.get_parent_index(current_idx)
            while self.heap[parent_idx] > self.heap[current_idx] and parent_idx >= 0:
                self.swap(parent_idx, current_idx)
                current_idx = parent_idx
                parent_idx = self.get_parent_index(current_idx)

    def remove(self):
        if len(self.heap) == 0:
            return False
        elif len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop()
            self.sink_down(0)
        return True

    def sink_down(self, index):
        left = self.get_left_child_index(index)
        right = self.get_right_child_index(index)
        min_heap = 0
        while True:
            if self.heap[left] < self.heap[index] and left < len(self.heap):
                min_heap = left
            if self.heap[right] < self.heap[index] and right < len(self.heap):
                min_heap = right
            if min_heap != index:
                self.swap(index, min_heap)
                min_heap = index
            else:
                return


myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]

"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]
"""