class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            j = 0
            for j in range(i + 1,len(nums)):
                if nums[j] <= nums[j - 1]:
                    ans = max(ans,j - i )
                    break
            else:
                ans = max(ans,j - i + 1)

            for j in range(i + 1,len(nums)):
                if nums[j] >= nums[j -1]:
                    ans = max(ans,j - i)
                    break
            else:   
                ans = max(ans,j - i + 1)

        return ans


