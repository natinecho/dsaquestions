class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        def trinagularSumm(nums):
            if len(nums) <=1 :
                return nums[0]
                
            l_pointer , r_pointer = 0,1
            newNums = []
            while r_pointer < len(nums):
                val = nums[l_pointer] + nums[r_pointer]
                newNums.append(val%10)
                l_pointer +=1
                r_pointer +=1
            return trinagularSumm(newNums)
        
        return trinagularSumm(nums)
        