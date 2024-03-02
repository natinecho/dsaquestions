class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr)<3:
            return False

        flag=arr[0]<arr[1]

        if not flag:
            return False

        count=0

        for i in  range(len(arr)-1):
            if arr[i]>arr[i+1] and count==0:
                count=1
                flag = not flag
            if (not flag and arr[i]<=arr[i+1]) or ( flag and arr[i]>=arr[i+1]) :
                return False
        
        return True if count==1 else False
        