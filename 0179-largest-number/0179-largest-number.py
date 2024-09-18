class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        nums.sort(key=lambda a: a * 10,reverse = True)

        if nums[0] == "0":
            return "0"

        return "".join(nums)
        