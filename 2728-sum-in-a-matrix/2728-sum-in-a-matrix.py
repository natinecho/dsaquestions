class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        maxx = []

        for i in range(len(nums)):
            nums[i] = sorted(nums[i])

        for i in range(len(nums[0])):
            temp = 0
            for j in range(len(nums)):
                temp = max(temp,nums[j][i])
            
            maxx.append(temp)

        return sum(maxx)

        