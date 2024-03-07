class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:  
        nums.sort()
        temp = target - nums[0]
        val = bisect_right(nums,temp)
        val = min(val, len(nums))
        count = 0

        l = 0
        r = val-1
        while l<=r :
            if nums[l] + nums[r] <= target:
                count = (count + 2 **(r-l))%((10**9) + 7)
                l += 1
            else:
                r -= 1


        return (count)%(10**9+7)

