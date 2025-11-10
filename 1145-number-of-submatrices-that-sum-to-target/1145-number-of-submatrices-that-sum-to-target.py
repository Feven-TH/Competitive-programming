class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r,c = len(matrix), len(matrix[0])
        for row in matrix:
            for j in range(1, c):
                row[j] += row[j - 1]
        
        res = 0
        for i in range(c):
            for j in range(i,c):
                maps = defaultdict(int)
                maps[0] = 1
                summ = 0 
                for k in range(r):
                    summ += matrix[k][j] - (matrix[k][i-1] if i> 0 else 0)
                    res += maps[summ - target] 
                    maps[summ] += 1
        return res