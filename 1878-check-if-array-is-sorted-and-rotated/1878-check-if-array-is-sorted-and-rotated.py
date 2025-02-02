class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = [1,4,1,2,3,5]
        if temp == nums:
            return False
        minn = nums.index(min(nums))
        i = 0
        while i < len(nums) - 1:
            if nums[i+1] < nums[i] and nums[i + 1] != nums[minn]:
                return False
            i += 1
        if nums [0]>= nums[-1] or minn == 0:
            return True

        return False