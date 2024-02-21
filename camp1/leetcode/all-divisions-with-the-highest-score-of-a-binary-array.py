class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones=sum(nums)
        zeros=0
        score=[]
        for i in nums:
            score.append(zeros+ones)
            if i==0:
                zeros+=1
            if i==1:
                ones-=1
        score.append(zeros+ones)

        num=max(score)
        
        res=[]

        for i,k in enumerate(score):
            if k ==num:
                res.append(i)
        return res
     