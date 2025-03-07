class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        Counts = Counter(arr)
        counts = {k: v for k, v in sorted(Counts.items(), key=lambda x: x[1], reverse=True)}
    
        half = len(arr) // 2
        res = 0
        for key,val in counts.items():
            if half <= 0:
                return res
            half -= val
            res += 1

        return res
        
