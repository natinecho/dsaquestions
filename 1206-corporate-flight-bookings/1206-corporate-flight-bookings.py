class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*(n+1)

        for i in bookings:
            res[i[0]-1] += i[2]
            res[i[1]] -= i[2]
        
        for i in range(1,len(res)):
            res[i] += res[i-1]
        
        return res[:-1]
        