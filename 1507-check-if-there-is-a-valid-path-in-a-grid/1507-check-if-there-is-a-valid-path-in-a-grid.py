class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        moves = {
            1: {'L': (0, -1), 'R': (0, 1)},
            2: {'U': (-1, 0), 'D': (1, 0)},
            3: {'L': (0, -1), 'D': (1, 0)},
            4: {'R': (0, 1), 'D': (1, 0)},
            5: {'L': (0, -1), 'U': (-1, 0)},
            6: {'R': (0, 1), 'U': (-1, 0)}
        }
        reverse = {(0, -1): 'R', (0, 1): 'L', (-1, 0): 'D', (1, 0): 'U'}
        
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])  
        
        root = {(i, j): (i, j) for i in range(len(grid)) for j in range(len(grid[i]))}
        rank = {(i, j): 0 for i in range(len(grid)) for j in range(len(grid[i]))}

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])  
            return root[x]
        
        def union(x, y):
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
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                curr = grid[i][j] 
                for move in moves[curr]:
                    temp = moves[curr][move]
                    row, col = i + temp[0], j + temp[1]
                    if inbound(row, col) and reverse[temp] in moves[grid[row][col]]:
                        union((i, j), (row, col))

        return find((0, 0)) == find((len(grid) - 1, len(grid[0]) - 1))
