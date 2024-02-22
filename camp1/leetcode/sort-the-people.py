class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr={}
        for i in range(len(heights)):
            arr[heights[i]]=names[i]
        heights.sort()
        res=[]
        for i in heights:
            res.append(arr[i]) 
        return res[::-1]