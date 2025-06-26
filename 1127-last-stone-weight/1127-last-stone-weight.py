class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heappush(heap, -s)
        while len(heap) >1:
            x,y = -heappop(heap), -heappop(heap)
            if x != y:
                heappush(heap, -(x-y))
        return -heap[0] if heap else 0

