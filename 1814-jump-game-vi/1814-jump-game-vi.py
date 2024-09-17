class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = [(- nums[-1], len(nums) - 1)]

        for i in range(len(nums) - 2, -1, -1):
            while heap:
                val,ind = heap[0]
                val = -val
                if ind >  i + k:
                    heappop(heap)
    
                else:
                    heappush(heap,(-(val + nums[i]),i))
                    break

        while heap:
            val,ind = heappop(heap)
            if ind == 0:
                return -val

        return -1