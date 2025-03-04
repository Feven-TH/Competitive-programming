class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        arrows = 1
        j = 0
        for i in range(1,len(points)):
            if points[i][0] > points[j][1] :
                arrows +=1
                j = i      
        return arrows



        