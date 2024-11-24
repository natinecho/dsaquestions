

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        

        front = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    front[i] = max(front[i], front[j] + 1)
        

        back = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    back[i] = max(back[i], back[j] + 1)
        

        max_mountain = 0
        for i in range(1, n - 1):  
            if front[i] > 1 and back[i] > 1: 
                max_mountain = max(max_mountain, front[i] + back[i] - 1)
        
        return n - max_mountain
