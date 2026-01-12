class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0 
        curr = points[0]
        for i in range(1,len(points)):
            p = points[i]
            res += max(abs(curr[0] - p[0]), abs(curr[1] - p[1]))
            curr = p
        return res
