class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        psum = 0
        ans = 0

        for i in range(len(nums)):
            psum += nums[i]
            ans = max(ceil(psum/(i+1)),ans)
        return ans
