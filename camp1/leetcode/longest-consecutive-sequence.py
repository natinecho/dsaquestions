class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sets=sorted(list(set(nums)))
        res=1
        temp=1
        if len(sets)==0:
            return 0
        for i in range(1,len(sets)):
            if sets[i]-sets[i-1]==1:
                temp+=1
            else:
                temp=1
            res=max(res,temp)
        return res