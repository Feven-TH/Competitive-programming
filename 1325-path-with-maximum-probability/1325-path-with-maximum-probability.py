class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for i in range(n)]
        for i,(u,v) in enumerate(edges):
            graph[u].append((v,succProb[i]))
            graph[v].append((u,succProb[i]))
        
        prob = [0 for i in range(n)]
        prob[start_node] = 1
        seen = set()
        
        heap = [(-1,start_node)]
        while heap:
            curr,node = heappop(heap)
            if node in seen:
                continue
            seen.add(node)
            for nei,pro in graph[node]:
                val = (-curr) * pro
                if val > prob[nei]:
                    heappush(heap, (-val,nei))
                    prob[nei] = val
        
        return prob[end_node] if prob[end_node] != 0 else 0
