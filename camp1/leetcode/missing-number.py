class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        d=Counter(nums)
        for i in range(len(nums)):
            if i not in d:
                return i
        return len(nums)
            
        