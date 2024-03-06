class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0

        l = 1
        r = x
        while l<=r:
            m = (l+r)//2
            if m**2 == x:
                return m
            elif m**2 >x:
                r = m-1
            else:
                ans = m
                l = m+1
        return ans
        