class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        maps = defaultdict(list)
        for i,j in edges:
            maps[i].append(j)
            maps[j].append(i)
        
        def dfs(node,target,visited):
            if node == target:
                return True
            
            visited.add(node)
            for i in maps[node]:
                if i not in visited:
                    found = dfs(i, target ,visited)
                    if found:
                        return True
            return False

        return dfs(source, destination , set())
                    