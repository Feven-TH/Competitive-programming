class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        colors = {col for row in targetGrid for col in row}
        # print(colors)
        bounds = {c: [m,n,-1,-1] for c in colors}  
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                bounds[c][0] = min(bounds[c][0],i)
                bounds[c][1] = min(bounds[c][1],j)
                bounds[c][2] = max(bounds[c][2],i)
                bounds[c][3] = max(bounds[c][3],j)

        graph = defaultdict(set)
        indegree = defaultdict(set)
        for c, (top,left,bottom,right) in bounds.items():
            for i in range(top, bottom + 1):
                for j in range(left, right + 1):
                    d = targetGrid[i][j]
                    if d != c:
                        graph[c].add(d)
                        indegree[d].add(c)
        
        q = deque(c for c in colors if len(indegree[c]) == 0)
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in graph[curr]:
                indegree[nei].discard(curr)
                if len(indegree[nei])== 0:
                    q.append(nei)
        
        return True if len(res) == len(colors) else False
        


