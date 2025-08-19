class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        maps = defaultdict(list)
        for i,r in enumerate(ring):
            maps[r].append(i)
        
        @lru_cache(None)
        def dfs(ringInd,keyInd):
            if len(key) == keyInd:
                return 0 
            minn = float('inf')
            for ind in maps[key[keyInd]]:
                diff = abs(ind - ringInd)
                steps = min(diff, len(ring) - diff) +1
                total = steps + dfs(ind, keyInd+1)
                minn = min(total, minn)
            return minn
        
        return dfs(0,0)
        
        