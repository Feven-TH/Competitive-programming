class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        diagonals = defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                diagonals[i+j].append(mat[i][j])
        
        res = []
        
        for k in range(rows + cols - 1):  
            if k % 2 == 0:
                res.extend(reversed(diagonals[k]))
            else:
                res.extend(diagonals[k])
        return res
