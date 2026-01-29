class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        prices = [[float('inf')]*26 for _ in range(26)]
        for u,v,w in zip(original, changed, cost):
            u,v = ord(u) - ord('a'), ord(v) - ord('a')
            prices[u][v] = min(prices[u][v], w)
        for i in range(26):
            prices[i][i] = 0
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    prices[i][j] = min(prices[i][j], prices[i][k] + prices[k][j])
                    
        res = 0 
        for s,t in zip(source,target):
            s,t = ord(s) - ord('a'), ord(t) - ord('a')
            if prices[s][t] == float('inf'):
                return -1
            res += prices[s][t]
        return res