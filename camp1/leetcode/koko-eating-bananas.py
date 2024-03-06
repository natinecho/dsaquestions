class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans =0

        while l<=r:
            m = (l+r)//2
            count = 0

            for i in range(len(piles)):
                count += ceil(piles[i]/m)

            if count > h:
                l = m+1
            else:
                ans = m
                r = m-1
        return ans

        