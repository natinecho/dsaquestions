class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        arr = [0]*(len(nums))
        l = 0

        for i in range(1,len(nums)):
            if nums[i] % 2 == nums[i -1] % 2 :
                l += 1
            arr[i] = l

        ans = []

        for st,end in queries:
            if arr[st] == arr[end]:
                ans.append(True) 
            else:
                ans.append(False)


        return ans
        


        