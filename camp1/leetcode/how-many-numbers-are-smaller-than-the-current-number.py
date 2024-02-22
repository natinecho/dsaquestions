class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=nums.copy()
        temp.sort(reverse=True)
        d={}
        ans=[]
        for i,v in enumerate(temp):
            d[v]=i

        for i,v in enumerate(nums):
            ans.append(len(nums)-(d[v]+1))

        return ans
        