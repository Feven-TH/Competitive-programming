class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        MOD = 10**9 + 7
        if complexity[0] >= min(complexity[1:]):
            return 0
        else:
            return factorial(n-1) % MOD