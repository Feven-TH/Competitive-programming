class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def validate(time):
            n = 0
            for r in ranks:
                n += int((time//r)**(0.5))
            return n >= cars

        high = max(ranks) * cars**2
        low = 1
        while low < high:
            mid = (low + high)//2
            # print(validate(mid))
            if validate(mid) :
                high = mid                 
            else:
                low = mid + 1
            
        return low


