class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = sorted(set(arr))
        di = {}

        for i in range(len(temp)):
            di[temp[i]] = i + 1
 
        for  i in range(len(arr)):
            arr[i] = di[arr[i]]

        return arr
        
        