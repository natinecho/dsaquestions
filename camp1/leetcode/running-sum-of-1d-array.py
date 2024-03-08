class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        psum = 0
        ans = []
        for i in range(len(nums)):
            psum +=nums[i]
            ans.append(psum)
        return ans
        