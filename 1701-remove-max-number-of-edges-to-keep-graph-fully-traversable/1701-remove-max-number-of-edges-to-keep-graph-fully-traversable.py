class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        rootA = [i for i in range(n + 1)]
        rankA = [0] * (n + 1)
        rootB = [i for i in range(n + 1)]
        rankB = [0] * (n + 1)
        
        def find(root, x):
            if root[x] != x:
                root[x] = find(root, root[x]) 
            return root[x]
        
        def union(root, rank, x, y):
            rootx = find(root, x)
            rooty = find(root, y)
            if rootx == rooty:
                return False
            if rank[rootx] > rank[rooty]:
                root[rooty] = rootx
            elif rank[rootx] < rank[rooty]:
                root[rootx] = rooty
            else:
                root[rooty] = rootx
                rank[rootx] += 1
            return True
        
        removed = 0
    
        for t, a, b in edges:
            if t == 3:
                connectedA = union(rootA, rankA, a, b)
                connectedB = union(rootB, rankB, a, b)
                if not connectedA and not connectedB:
                    removed += 1
        
        for t, a, b in edges:
            if t == 1:
                if not union(rootA, rankA, a, b):
                    removed += 1
        
        for t, a, b in edges:
            if t == 2:
                if not union(rootB, rankB, a, b):
                    removed += 1
        
        set_A = set(find(rootA, i) for i in range(1, n + 1))
        set_B = set(find(rootB, i) for i in range(1, n + 1))
        
        if len(set_A) > 1 or len(set_B) > 1:
            return -1
            
        return removed
