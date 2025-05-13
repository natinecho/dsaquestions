class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n

        while l + 1 < r:
            mid = (l + r)//2

            val = (mid * (mid + 1))//2

            if val <= n:
                l = mid
            else:
                r = mid 

        return l


        