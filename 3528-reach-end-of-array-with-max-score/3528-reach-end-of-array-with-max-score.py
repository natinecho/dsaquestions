class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ind = 0
        score = 0

        for i in range(len(nums)):
            if nums[i] > nums[ind]:
                score += (i - ind) * nums[ind]
                ind = i

        score += (i - ind) * nums[ind]
        return score