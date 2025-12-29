class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        maps = defaultdict(list)
        for p in allowed:
            maps[p[:2]].append(p[-1])
        
        memo = {}
        def dp(curr, nxt):
            if len(curr) == 2 and len(nxt) == 1:
                return True
            if len(nxt) == len(curr) - 1:
                return dp(nxt, "")
            
            state = (curr, nxt)
            if state in memo:
                return memo[state]

            i = len(nxt)
            pair = curr[i:i+2]
        
            for top in maps.get(pair, []):
                if dp(curr, nxt +top):
                    memo[state] = True
                    return True

            memo[state] = False
            return False

        return dp(bottom, "")