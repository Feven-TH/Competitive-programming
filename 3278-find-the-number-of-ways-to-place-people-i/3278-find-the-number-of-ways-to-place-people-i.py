class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0
        points.sort(key=lambda p:(p[0],-p[1]))

        for i in range(n):
            for j in range(i+1, n):
                xA, yA = points[i]
                xB, yB = points[j]
                
                if yA >= yB:
                    empty = True
                    for k in range(i + 1, j):
                        xk,yk = points[k]
                        if yB <= yk <= yA:
                            empty = False
                            break
                    if empty:
                        count += 1 
        return count