class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        temp=[]
        res=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        for i in range(len( nums)):
            if nums[i] ==0:
                temp.append(nums[i])
            else:
                res.append(nums[i])
        res.extend(temp)
        return res
                
        
        
        