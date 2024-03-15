class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        c = 0
        maxx = 0

        if 1 not in nums:
            return k

        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            
            while c > k:
                if nums[l] == 0:
                    c -= 1
                l += 1
            maxx = max(maxx,i - l)
        
        return maxx + 1
        