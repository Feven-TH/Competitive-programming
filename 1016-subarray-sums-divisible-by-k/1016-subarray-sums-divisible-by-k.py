class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        maps = {0:1}
        prefix = 0
        counts = 0
        for i in nums:
            prefix += i
            if prefix % k in maps:
                counts += maps[prefix % k]
            maps[prefix % k] = maps.get(prefix % k, 0) + 1
        return counts

        