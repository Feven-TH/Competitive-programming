class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        for freq in count.values():
            heappush(heap, -freq)
        
        interval = 0
        while heap:
            cycle = n + 1
            remaining = []
            
            prev_count = 0
            for i in range(cycle):
                if heap:
                    prev_count += 1
                    freq = -heappop(heap)
                    freq -= 1
                    if freq > 0:
                        remaining.append(-freq)
            
            for freq in remaining:
                heappush(heap, freq)
            if heap:
                interval += cycle
            else:
                interval += prev_count
           
        return interval
