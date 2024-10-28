class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        di = {}
        nums.sort(reverse = True)

        for i in nums:
            if i not in di:
                if i * i in  di:
                    di[i] = di[i * i] + 1
                else:
                    di[i] = 1
        
        maxx = 0
        for i in di.values():
            maxx = max(maxx,i)

        return -1 if maxx == 1 else maxx
                    