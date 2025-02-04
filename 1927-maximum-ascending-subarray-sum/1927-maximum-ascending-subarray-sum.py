class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxx = nums[0]
        summ = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= nums[i -1]:
                maxx = max(maxx,summ)
                summ = 0

            summ += nums[i]

        maxx = max(summ, maxx)

        return maxx
        