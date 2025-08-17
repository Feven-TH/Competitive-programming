"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def uniform(row,col, size):
            first, flag = grid[row][col], True
            for r in range(row, row+size):
                for c in range(col ,col + size):
                    if valid(r,c) and grid[r][c] != first:
                        flag = False
            return flag
        
        def dfs(row,col,size):
            if uniform(row,col,size):
                return Node(val = bool(grid[row][col]), isLeaf = True)
            else:
                half = size//2
                return  Node(True, False,
                dfs(row, col, half),
                dfs(row, col + half, half),
                dfs(row + half, col, half),
                dfs(row + half, col + half, half)
            )

        return dfs(0, 0, len(grid))
                
