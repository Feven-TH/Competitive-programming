class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        #print(graph)
        visited = set()

        def complete(component):
            size = len(component)
            edges = 0
            for c in component:
                edges += len(graph[c])
            return edges//2 == size * (size - 1) // 2

        def dfs(vertex , component):
            component.append(vertex)
            visited.add(vertex)
            for c in graph[vertex]:
                if c not in visited:
                    dfs(c , component)

        res = 0
        for i in graph:
            if i not in visited:
                component = []
                dfs(i , component)
                if complete(component):
                    res += 1
        return res



       

        