class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            if len(heap) < k:
                heap.append(point)
                self.sift_up(heap, len(heap) - 1)
            else:
                if self.get_distance(point) < self.get_distance(heap[0]):
                    heap[0] = point
                    self.sift_down(heap, 0)
        return heap

    def get_distance(self, point):
        x, y = point
        return (x**2 + y**2) ** 0.5

    def sift_up(self, heap, i):
        p = (i - 1) // 2
        if p >= 0 and self.get_distance(heap[p]) < self.get_distance(heap[i]):
            heap[p], heap[i] = heap[i], heap[p]
            self.sift_up(heap, p)

    def sift_down(self, heap, i):
        l = 2 * i + 1
        r = 2 * i + 2
        largest = i
        if l < len(heap) and self.get_distance(heap[l]) > self.get_distance(heap[largest]):
            largest = l

        if r < len(heap) and self.get_distance(heap[r]) > self.get_distance(heap[largest]):
            largest = r

        if largest != i:
            heap[largest], heap[i] = heap[i], heap[largest]
            self.sift_down(heap, largest)
