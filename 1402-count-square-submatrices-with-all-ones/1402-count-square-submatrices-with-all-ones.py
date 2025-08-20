class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def allOnes(row,col,size):
            for r in range(row,row+size):
                for c in range(col, col+size):
                    if matrix[r][c] != 1:
                        return False
            return True
        
        count = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxx = min(len(matrix)-r, len(matrix[0])-c)
                for size in range(1, maxx+1):
                    if allOnes(r,c,size):
                        count += 1
                    else:
                        break
        return count 
    