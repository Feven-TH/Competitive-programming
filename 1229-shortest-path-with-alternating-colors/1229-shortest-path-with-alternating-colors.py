class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        blues = defaultdict(list)
        reds = defaultdict(list)
        
        for u, v in redEdges:
            reds[u].append(v)
        for u, v in blueEdges:
            blues[u].append(v)
        
        res = [-1 for _ in range(n)]
        q = deque()
        q.append([0, 0, None])
        visited = set()
        visited.add((0,None))

        while q:
            curr, length , color = q.popleft()
            if res[curr] == -1:
                res[curr] = length

            if color != "Blue":
                for i in blues[curr]:
                    if (i,"Blue") not in visited:
                        visited.add((i, "Blue"))
                        q.append([i ,length + 1, "Blue"])
            if color != "Red":
                for i in reds[curr]:
                    if (i,"Red") not in visited:
                        visited.add((i, "Red"))
                        q.append([i ,length + 1, "Red"])
        return res                


        
