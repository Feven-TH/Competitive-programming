class SeatManager:

    def __init__(self, n: int):
       self.nums = [i for i in range(1,n+1)]

    def reserve(self) -> int:
        return heappop(self.nums)
    
    def unreserve(self, seatNumber: int) -> None:
        heappush(self.nums,seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)