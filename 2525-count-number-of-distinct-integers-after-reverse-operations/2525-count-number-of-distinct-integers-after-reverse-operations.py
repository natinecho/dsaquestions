class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinict = set(nums)
        
        for i in nums:
            rev = int(str(i) [::-1] )
            distinict.add(rev)
        
        return len(distinict)
