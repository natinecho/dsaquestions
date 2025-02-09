class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        di = Counter()

        count = 0
        n = len(nums)

        for i in range(n):
            di[nums[i] - i] += 1
            
        for val in di.values():
            count +=(val *(val + 1))//2


        return ((n *(n + 1))//2) - count