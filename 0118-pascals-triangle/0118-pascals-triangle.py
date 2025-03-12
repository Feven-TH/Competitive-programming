class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        def pascal(n):
            if n == 0:
                ans.append([1])
                return [1]

            upper = pascal(n-1) # 1 2 1
            new_row = [1]*(len(upper) + 1)
            for i in range(1, len(upper)):
                new_row[i] = upper[i - 1] + upper[i]
            ans.append(new_row)
            return new_row
        pascal(numRows - 1)
        return ans