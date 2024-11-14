class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l = 1
        r = max(quantities)

        def check(val):
            cc = 0
            for nn in quantities:
                cc += ceil(nn / val)
            return cc <= n

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
