class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        for node in range(len(graph)):
            if node not in visited:
                q = deque([node])
                visited[node] = 0
                while q:
                    node = q.popleft()
                    for n in graph[node]:
                        if n in visited and visited[n] == visited[node]:
                            return False
                        if n not in visited:
                            visited[n] = visited[node] ^ 1
                            q.append(n)
        return True 