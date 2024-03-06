class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l = 0
        r = len(nums)-1
        if len(nums) == 2:
            return min(nums)
            
        while l <= r:
            mid = (l+r)//2
            if nums[mid] > ans:
                l = mid +1
            else:
                ans = min(ans, nums[mid])
                r = mid -1

        return ans

        