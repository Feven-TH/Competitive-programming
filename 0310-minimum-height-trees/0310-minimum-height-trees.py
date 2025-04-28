class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = [[] for i in range(n)]
        incoming = [0]*n
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            incoming[u] += 1
            incoming[v] += 1
        
        q = deque()
        for i in range(len(incoming)):
            if incoming[i] == 1:
                q.append(i)
        
        res = []
        while q:
            res = []
            for i in range(len(q)):
                curr = q.popleft()
                res.append(curr)

                for nei in graph[curr]:
                    incoming[nei] -= 1
                    if incoming[nei] ==  1:
                        q.append(nei)
        return res
            

