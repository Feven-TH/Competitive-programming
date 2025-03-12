class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascal(n):
            if n == 0:
                return [1]

            upper = pascal(n-1) # 1 2 1
            new_row = [1]*(len(upper) + 1)
            for i in range(1, len(upper)):
                new_row[i] = upper[i - 1] + upper[i]
            return new_row
        return pascal(rowIndex)