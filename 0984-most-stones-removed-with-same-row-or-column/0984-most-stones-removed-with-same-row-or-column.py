class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        root = {i:i for i in range(len(stones))}
        rank = {i:0 for i in range(len(stones))}
        
        def find(x):
            if root[x] == x:
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
        
        for i in range(len(stones)):
            for j in range(len(stones)):  
                if i != j and (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]):
                    union(i,j)
        # print(root)
        return len(stones) - len(set(find(i) for i in root))