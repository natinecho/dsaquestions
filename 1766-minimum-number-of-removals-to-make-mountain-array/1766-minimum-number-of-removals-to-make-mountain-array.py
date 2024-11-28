class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        front = [0] * n
        lis = []
        for i in range(n):
            pos = bisect_left(lis, nums[i])
            if pos == len(lis):
                lis.append(nums[i])
            else:
                lis[pos] = nums[i]
            front[i] = pos + 1
        
        back = [0] * n
        lis = []
        for i in range(n - 1, -1, -1):
            pos = bisect_left(lis, nums[i])
            if pos == len(lis):
                lis.append(nums[i])
            else:
                lis[pos] = nums[i]
            back[i] = pos + 1
        
        maxx = 0
        for i in range(1, n - 1):  
            if front[i] > 1 and back[i] > 1: 
                maxx = max(maxx, front[i] + back[i] - 1)
        
        return n - maxx
