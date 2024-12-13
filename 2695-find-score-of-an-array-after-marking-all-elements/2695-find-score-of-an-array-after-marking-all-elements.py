class Solution:
    def findScore(self, nums: List[int]) -> int:

        arr = [(num,ind ) for ind,num  in enumerate(nums)]
        arr.sort()
        
        added = set()
        score =  0

        for num,ind in arr:
            if ind not in added:
                score += num
                added |= {ind,ind-1,ind + 1}
        
                

        return score
        