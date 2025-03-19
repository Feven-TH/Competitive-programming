class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(i):
            if len(path) == k:
                res.append(path.copy())
                return 
            if i > n:
                return
            path.append(i)
            backtrack(i + 1)

            path.pop()
            backtrack(i + 1)
        
        backtrack(1)
        return res