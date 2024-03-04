class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backTrack(n,path):
            ans.append(path[:])
            if len(path)== len(nums):
                return 
             
            for i in range(n,len(nums)):
                path.append(nums[i])
                backTrack(i+1,path)
                path.pop()

        ans = []
        
        backTrack(0, [])

        return ans

