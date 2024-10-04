class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(val):
            count = 0
            for i in range(len(candies)):
                count += (candies[i] // val)
            return count

        l = 1
        r = max(candies)
        ans = 0

        while l <= r:
            mid = (l + r)//2
            temp = check(mid)
            if temp >= k:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans