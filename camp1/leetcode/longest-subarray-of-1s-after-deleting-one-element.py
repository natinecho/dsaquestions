class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        c = 0
        maxx = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            while c > 1:
                if nums[l] == 0:
                    c -= 1
                l += 1
            maxx = max(maxx,i - l )

        return maxx

            



        