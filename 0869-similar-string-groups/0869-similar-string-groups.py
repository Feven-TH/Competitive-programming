class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        root = {i:i for i in range(n)}
        rank = {i:0 for i in range(n)}

        def countDifference(x,y):
            return sum(a!=b for a,b in zip(x,y))
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    root[rooty] = rootx
                elif rank[rootx] < rank[rooty]:
                    root[rootx] = rooty
                else:
                    root[rooty] = rootx
                    rank[rootx] += 1
        
        
        for i in range(n):
            for j in range(i+1,n):
                if countDifference(strs[i], strs[j]) <= 2:
                    union(i,j)
        
        return len(set(find(i) for i in root))


