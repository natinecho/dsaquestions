class SeatManager:

    def __init__(self, n: int):
        self.st = [i for i in range(1,n + 1)]
        

    def reserve(self) -> int:
        return heappop(self.st)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.st,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)