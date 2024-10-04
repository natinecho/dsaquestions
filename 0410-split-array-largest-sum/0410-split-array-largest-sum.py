from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def check(summ):
            val = 0
            count = 1  

            for i in range(len(nums)):
                val += nums[i]
                if val > summ:
                    count += 1
                    val = nums[i] 

            return count

        l = max(nums)
        r = sum(nums)

        ans = 0
        while l <= r:
            mid = (l + r) // 2

            if check(mid) <= k:  
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
