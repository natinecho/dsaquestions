from heapq import heappop, heappush

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        arr = []
        chair = []
        heap = []
        
        for i in range(len(times)):
            arr.append((times[i][0], times[i][1], i))
        
        arr.sort() 

        for i in range(len(times)):
            heappush(chair, i)
        
        for arrival, leaving, ind in arr:
            while heap and heap[0][0] <= arrival:
                ll , chno = heappop(heap)
                heappush(chair, chno) 
            
            seat = heappop(chair)
            heappush(heap, (leaving, seat)) 

            if ind == targetFriend:
                return seat
        
        return -1
