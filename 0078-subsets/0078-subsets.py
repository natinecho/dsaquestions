class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        n = len(nums)

        for  bit in range(1<<n):
            temp = []
            for  i in range(n):
                if bit & (1<<i):
                    temp.append(nums[i])
            path.append(temp)
        
        return path
