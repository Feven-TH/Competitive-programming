class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for i in range(n + 1)]
        for u, v ,t in times:
            graph[u].append((v,t))
        
        delay = {i: float('inf') for i in range(1,n+1)}
        delay[k] = 0
        heap = [(k,0)]
       
        while heap:
            v , t = heappop(heap)
            if t > delay[v]:
                continue

            delay[v] = t
            for nei,time in graph[v]:
                if delay[nei] > time + t:
                    delay[nei] = time + t
                    heappush(heap ,(nei, time +t))
        
        minn = max(delay.values())
        return minn if minn != float('inf') else -1
                

       
