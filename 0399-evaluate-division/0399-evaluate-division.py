class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        maps = defaultdict(list)
        for i in range(len(equations)):
            u , v = equations[i]
            val = values[i]
            maps[u].append((v ,val))
            maps[v].append((u ,1/val))
        
        def bfs(start,end):
            if start not in maps or end not in maps:
                return -1.0
                
            seen = set()
            q = deque([(start , 1.0)])
            while q:
                curr, product = q.popleft()
                if curr == end:
                    return product
                for node, val in maps[curr]:
                    if node not in seen:
                        seen.add(node)
                        q.append((node, product*val))
            return -1.0
        
        res = []
        for start,end in queries:
            res.append(bfs(start,end))
        
        return res



        