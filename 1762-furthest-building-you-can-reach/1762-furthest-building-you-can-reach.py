class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                bricks  -= diff
                heappush(heap,-diff)

                if bricks < 0 and ladders > 0:
                    Sub_brick = -heappop(heap)
                    ladders -= 1
                    bricks += Sub_brick
                
                if bricks < 0 and ladders == 0:
                    return i

            
        return len(heights) - 1

        

                





