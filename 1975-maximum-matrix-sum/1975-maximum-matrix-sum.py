class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0 
        minn = float('inf') 
        negatives = 0 
        for row in matrix: 
            for num in row: 
                abs_num = abs(num) 
                total += abs_num 
                minn = min(minn, abs_num) 
                if num < 0: 
                    negatives += 1 
        if negatives % 2 == 0: 
            return total 
        else: 
            return total - 2 * minn