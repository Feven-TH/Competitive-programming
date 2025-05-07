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
        
        row = defaultdict(list)
        for i in range(len(stones)):
            row[stones[i][0]].append(i)
        
        col = defaultdict(list)
        for i in range(len(stones)):
            col[stones[i][1]].append(i)

        for r in row:
            for i in range(1, len(row[r])): 
                union(row[r][i-1], row[r][i])
        for c in col:
            for i in range(1, len(col[c])):
                union(col[c][i-1], col[c][i])
        
        
        return len(stones) - len(set(find(i) for i in root))