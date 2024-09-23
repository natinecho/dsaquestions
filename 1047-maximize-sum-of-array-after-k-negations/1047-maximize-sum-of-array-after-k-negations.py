class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        summ = 0
        nums.sort(key = lambda x: abs(x), reverse = True)

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                k -= 1
                nums[i] = abs( nums[i])

            summ += nums[i]

        if k > 0:
            summ -= min(nums)
            summ += -min(nums) if k %2 == 1 else min(nums)


        return summ

        