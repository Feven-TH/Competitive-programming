class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        maps = [[] for _ in range(n)]
        indegree = [0 for i in range(n)]
        for u, v in edges:
            maps[v].append(u)
            indegree[v] += 1
        
        res = [set() for _ in range(n)]
        q = deque([i for i in range(n) if indegree[i]==0])
        while q:
            curr = q.popleft()
            for child in [v for v in range(n) if curr in maps[v]]:
                res[child].add(curr)
                res[child].update(res[curr])
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)
        return [sorted(list(r)) for r in res]
    

        


        
                