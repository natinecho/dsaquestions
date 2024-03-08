class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        psum = 0
        nums.append(0)
        summ = sum(nums)
        for i in range(len(nums)-1):
            val = summ - (nums[i] + psum)
            if psum == val:
                 return i
            psum += nums[i]
        return -1
        