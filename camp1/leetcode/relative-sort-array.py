class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    res.append(j)
        temp=[]
        for j in arr1:
            if j not in res:
                temp.append(j)
        if temp:
            temp.sort()
            res.extend(temp)
                
        return res
        