class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num=0
        for i in range(len(nums)):
            if num<i:
                return False
            num=max(num,i+nums[i])          
        return True 