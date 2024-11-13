class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0

        for i in range(len(nums)):
            ll = bisect_left(nums, lower - nums[i], i + 1)
            uu = bisect_right(nums, upper - nums[i], i + 1)
            
            ans += (uu - ll)

        return ans
