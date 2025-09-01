class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calculate(passed,total):
            return (passed+ 1) /(total+ 1) - passed/total

        maxx = []
        for p,t in classes:
            gain = calculate(p,t)
            heapq.heappush(maxx,(-gain,p,t))
        
        for _ in range(extraStudents):
            neg_gain,p,t = heapq.heappop(maxx)
            p += 1
            t += 1
            new_gain = calculate(p, t)
            heapq.heappush(maxx, (-new_gain,p,t))
        
        ratio = 0
        while maxx:
            _,p,t = heapq.heappop(maxx)
            ratio += p/t
        
        return ratio/len(classes)