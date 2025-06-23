class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        root = {i:i for i in range(n)}
        rank = {i:0 for i in range(n)}
        res = [-1]*n

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
        edgeList.sort(key = lambda x:x[2])
        queries = sorted([(p,q,limit,i)for i,(p,q,limit) in enumerate(queries)],key=lambda x:x[2])

        res = [False]*len(queries)
        idx = 0  

        for p, q, limit, i in queries:
            while idx < len(edgeList) and edgeList[idx][2] < limit:
                u, v, w = edgeList[idx]
                union(u, v)
                idx += 1
            if find(p) == find(q):
                res[i] = True

        return res