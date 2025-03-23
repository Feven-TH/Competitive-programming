class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        seen = set()

        def backtrack(curr):
            if len(curr) == len(pattern) + 1:
                result.append("".join(curr))
                return

            for i in map(str, range(1, 10)): 
                if i in seen:
                    continue
               
                n = len(curr)
                if n == 0 or (
                    pattern[n - 1] == 'I' and curr[-1] < i) or (
                    pattern[n - 1] == 'D' and curr[-1] > i):
                    
                    curr.append(i)
                    seen.add(i)
                    
                    backtrack(curr)
                    
                    curr.pop()
                    seen.remove(i)

        backtrack([])
        return min(result)
