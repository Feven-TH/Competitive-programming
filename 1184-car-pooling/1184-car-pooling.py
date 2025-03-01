class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix = [0] * 1002
        for i in trips:
            prefix[i[1]] += i[0]
            prefix[i[2]] -= i[0]
        
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        
        if max(prefix) > capacity:
            return False
        else:
            return True