class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        total = set(freq1.keys()).union(freq2.keys())
        total_freq = Counter()
        for fruit in total:
            temp = freq1[fruit] +freq2[fruit]
            if temp %2 != 0:
                return -1 
            total_freq[fruit] = temp
        
        target = {}
        for fruit in total_freq:
            target[fruit] = total_freq[fruit]//2
        
        excess1 = []
        excess2 = []
        for fruit in total_freq:
            diff1 = freq1[fruit] - target[fruit]
            diff2 = freq2[fruit] - target[fruit]

            if diff1 > 0:
                excess1.extend([fruit] * diff1)
            if diff2 > 0:
                excess2.extend([fruit] * diff2)
        
        excess1.sort()
        excess2.sort(reverse=True)
        minn = min(total)
        cost = 0

        for a,b in zip(excess1,excess2):
            swap_cost = min(a,b)
            double_cost = 2*minn
            cost += min(swap_cost, double_cost)
        return cost