# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l ,r = 1,n
        minn = float('inf')

        while l<=r:
            n = (r+l)//2
            if isBadVersion(n):
                r =n-1
                minn = n
            else:
                l = n+1
        return  minn
        