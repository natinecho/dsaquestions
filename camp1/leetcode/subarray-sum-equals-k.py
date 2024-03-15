class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di = {0:1}
        count = 0
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            if summ - k  in di:
                count += di[summ - k]
            
            if summ in di:
                di[summ] += 1
            else:
                di[summ ] = 1
                


        return count
            