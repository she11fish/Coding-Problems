class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i, stone in enumerate(stones):
            if len(heap) < 2:
                heap.append(i)
                heap.sort(key=lambda j: stones[j])
            else:
                if stone > stones[heap[0]]:
                    heap[0] = i
                    heap.sort(key=lambda j: stones[j])
        while len(heap) == 2:            
            if stones[heap[0]] == stones[heap[1]]:
                if heap[0] <= heap[1]:
                    stones.pop(heap[1])
                    stones.pop(heap[0])
                else:
                    stones.pop(heap[0])
                    stones.pop(heap[1])
                heap = []
            else:
                mini = heap[0]
                maxi = heap[1]
                diff = stones[maxi] - stones[mini]
                stones[maxi] = diff
                stones.pop(mini)
                heap.pop(0)
                if mini < maxi:
                    heap[0] -= 1
            for i, stone in enumerate(stones):
                if i in heap:
                    continue
                if len(heap) < 2:
                    heap.append(i)
                    heap.sort(key=lambda j: stones[j])
                else:
                    if stone > stones[heap[0]]:
                        heap[0] = i
                        heap.sort(key=lambda j: stones[j])
        if not stones:
            return 0
        return stones[0]
