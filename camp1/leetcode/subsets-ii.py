class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        sets = set()

        def backTrack(i):

            sets.add(tuple(sorted(path.copy())))


            if len(path) == len(nums):
                return 

            for j in range(i,len(nums)):
                path.append(nums[j])
                backTrack(j+1)
                path.pop()
        
        backTrack(0)

        return list(sets)