class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        arrows = 1
        j = len(points) - 1
        for i in range(len(points) - 2, - 1 , - 1):
            if points[i][1] < points[j][0] :
                arrows +=1
                j = i      
        return arrows



        