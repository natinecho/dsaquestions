class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []

        di ={}
        def backTrack(i):
            if len(nums) == len(path):
                ans.append(path.copy())  
                return 
            
            for j in range(len(nums)):
                if nums[j] not in di:
                    path.append(nums[j])
                    di[nums[j]] = 1
                    backTrack(j+1)
                    path.pop()
                    del di[nums[j]]

        backTrack(0)

        return ans



        