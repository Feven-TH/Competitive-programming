class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n+1)]
        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        # print(graph)
        res = float('inf')
        visited = set()
        def dfs(i):
            nonlocal res
            if i in visited:
                return
            visited.add(i) 
            for nei,w in graph[i]:
                res = min(res,w)
                dfs(nei)
        dfs(1)
        return res

                
    