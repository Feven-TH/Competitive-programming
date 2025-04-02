class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for _ in range(n)] 
        counts = Counter(nums)
        for key , val in counts.items():
            bucket[val - 1].append(key)
        
        res = []
        for i in range(n-1, -1 , -1):
            if len(res) == k:
                return res
            for j in bucket[i]:
                res.append(j)
        return res