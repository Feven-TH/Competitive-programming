class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def validate(mid):
            prev = position[0]
            count = 1
            for i in range(1 , len(position)):
                curr = position[i]
                if curr - prev >= mid:
                    prev = curr
                    count += 1
                if count == m:
                    return True
            return False
        
        position.sort()
        low = 1
        high = 2**40
        res = low
        while low <= high:
            mid = (low + high)//2
            if validate(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
