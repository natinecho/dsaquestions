class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans = 0

        maxx = max(nums)

        while k > 0:
            ans += maxx
            maxx += 1
            k -= 1

        return ans

        