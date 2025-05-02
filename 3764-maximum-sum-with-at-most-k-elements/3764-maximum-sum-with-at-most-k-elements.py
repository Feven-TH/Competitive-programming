class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        for row in grid:
            row.sort(reverse = True)
        heap = []
        for i in range(len(limits)):
            for j in range(limits[i]):
                heappush(heap, (-grid[i][j], i))
                
        summ = 0
        count = 0
        while heap and count < k:
            curr, row = heappop(heap)
            curr = -curr
            summ += curr
            count += 1
        return summ

