class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = [num%2 for num in nums]
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
       
        maps = defaultdict(int)
        maps[0] = 1
        counts = 0
        for p in prefix:
            counts += maps[p - k]
            maps[p] += 1
        return counts