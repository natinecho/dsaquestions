class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num=len(arr)//4
        d=defaultdict(int)
        for i in arr:
            d[i]+=1
        res=max(d,key=lambda x:d[x])
        return res