class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        summ = sum(nums)
        temp = 0

        for val in nums:
            temp += sum(map(int,list(str(val))))

        return abs(summ - temp)
