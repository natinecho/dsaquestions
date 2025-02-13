class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operation = 0
        
        while len(nums) >= 2 and nums[0] < k:
            val = heappop(nums)
            val2 = heappop(nums)
            operation += 1

            heappush(nums,min(val, val2) * 2 + max(val, val2))
        
        return operation