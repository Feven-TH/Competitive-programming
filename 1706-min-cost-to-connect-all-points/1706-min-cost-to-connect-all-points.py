class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(x,y):
            return abs(x[0] - y[0]) + abs(x[1]- y[1])
        
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                edges.append((dist(points[i],points[j]),i,j))
        
        edges.sort()
        
        root = {i:i for i in range(len(points))}
        rank = {i:0 for i in range(len(points))}
        def find(x):
            if root[x] == x:
                return x
            root[x] = find(root[x])  
            return root[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    root[rooty] = rootx
                elif rank[rootx] < rank[rooty]:
                    root[rootx] = rooty
                else:
                    root[rooty] = rootx
                    rank[rootx] += 1
        
        res = 0
        count = 0
        for w,u,v in edges:
            if find(u) != find(v):
                union(u,v)
                res += w
                count += 1
                if count == len(points) -1:
                    return res
        return 0

       

