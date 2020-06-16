class MaxHeap:
    def __init__(self):
        self.heap = [None]
        self.length = 0

    def insert(self, val) -> None:
        self.heap.append(val)
        self.length += 1
        child = self.length
        parent = child // 2

        while parent > 0:
            if self.heap[parent] < self.heap[child]:
                self.heap[parent], self.heap[child] = (
                    self.heap[child],
                    self.heap[parent],
                )
                child = parent
                parent = child // 2
            else:
                break

        return

    def delete(self) -> int:
        if self.length == 0:
            return None
        if self.length == 1:
            self.length -= 1
            return self.heap.pop()
        else:
            last = self.length
            self.heap[1], self.heap[last] = self.heap[last], self.heap[1]
            val = self.heap.pop()
            self.length -= 1

            parent = 1
            left = parent * 2
            right = left + 1

            while left <= self.length or right <= self.length:
                
                if self.heap[left] > self.heap[parent]:
                    largest = left
                else:
                    largest = parent
                if right <= self.length and self.heap[right] > self.heap[largest]:
                    largest = right
                if largest != parent:
                    self.heap[largest], self.heap[parent] = self.heap[parent], self.heap[largest]
                else:
                    break
                parent = largest
                left = parent * 2
                right = left + 1
                
            return val

    def max(self) -> int:
        return self.heap[1] if self.length > 0 else None


class MinHeap:
    def __init__(self):
        self.heap = [None]
        self.length = 0

    def insert(self, val) -> None:
        self.heap.append(val)
        self.length += 1
        child = self.length
        parent = child // 2

        while parent > 0:
            if self.heap[parent] > self.heap[child]:
                self.heap[parent], self.heap[child] = (
                    self.heap[child],
                    self.heap[parent],
                )
                child = parent
                parent = child // 2
            else:
                break

        return

    def delete(self) -> int:
        if self.length == 0:
            return None
        if self.length == 1:
            self.length -= 1
            return self.heap.pop()
        else:
            last = self.length
            self.heap[1], self.heap[last] = self.heap[last], self.heap[1]
            val = self.heap.pop()
            self.length -= 1

            parent = 1
            left = parent * 2
            right = left + 1

            while left <= self.length or right <= self.length:
                
                if self.heap[left] < self.heap[parent]:
                    smallest = left
                else:
                    smallest = parent
                if right <= self.length and self.heap[right] < self.heap[smallest]:
                    smallest = right
                if smallest != parent:
                    self.heap[smallest], self.heap[parent] = self.heap[parent], self.heap[smallest]
                else:
                    break
                parent = smallest
                left = parent * 2
                right = left + 1

            return val

    def min(self) -> int:
        return self.heap[1] if self.length > 0 else None
