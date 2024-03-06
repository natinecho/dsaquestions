class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        ans = 0
        while l<=r:
            m = (l+r)//2
            summ = 0
            for i in range(len(nums)):
                summ += ceil(nums[i]/m)
            
            if summ > threshold:
                l = m + 1
            else:
                ans = m
                r = m - 1

        return ans
        