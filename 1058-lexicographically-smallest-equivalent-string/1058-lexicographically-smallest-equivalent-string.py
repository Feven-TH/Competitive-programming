class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i): chr(i) for i in range(97, 124)}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                minn = min(rootX, rootY)  
                parent[rootX] = parent[rootY] = minn

        for a, b in zip(s1, s2):
            union(a, b)
        return "".join(parent[find(c)] for c in baseStr)