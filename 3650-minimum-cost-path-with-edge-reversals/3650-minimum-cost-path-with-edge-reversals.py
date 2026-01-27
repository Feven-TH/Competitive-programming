class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,2*w))
        
        dist = [float('inf')]*n
        dist[0] = 0
        heap = [(0,0)]
        while heap:
            d,u = heappop(heap)
            if dist[u] < d:
                continue
            for nei,w in graph[u]:
                if dist[nei] > dist[u] + w:
                    dist[nei] = dist[u] + w
                    heappush(heap, (dist[nei],nei))
            
        return dist[-1] if dist[-1] != float('inf') else -1
            
