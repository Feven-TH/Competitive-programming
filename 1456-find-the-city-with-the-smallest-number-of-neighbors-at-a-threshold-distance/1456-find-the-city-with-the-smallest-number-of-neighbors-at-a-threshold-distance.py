class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for i in range(n)]
        for i,j,w in edges:
            dist[i][j] = w
            dist[j][i] = w
        for i in range(n):
            dist[i][i] = 0 
        
        for k in range(n):
            for j in range(n):
                for i in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        # print(dist)
        ans,res = -1, float(inf)
        for i in range(n):
            curr = 0
            for d in dist[i]:
                if 0 < d <= distanceThreshold:
                    curr += 1
            if curr <= res:
                ans = i
                res = curr
        return ans
                           
                
                