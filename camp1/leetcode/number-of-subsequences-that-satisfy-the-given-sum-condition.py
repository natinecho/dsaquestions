class Solution:
    def numSubseq(self, nums, target):
        nums.sort()
        count = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] + nums[r] <= target:
                count = (count + 2**(r-l)) % (10**9 + 7)
                l += 1
            else:
                r -= 1
        
        return count