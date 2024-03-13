class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = 0 
        temp = 0
        l = 0
        for i in range(len(nums)):
            if i<k:
                temp += nums[i]
                summ = temp
            else:
                temp = temp - nums[l] + nums[i]
                summ = max(summ,temp)
                l += 1

        return summ/k




            
        