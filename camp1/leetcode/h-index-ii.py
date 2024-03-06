class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = -1
        l = 0
        r = len(citations)

        while l<=r:
            m = (l+r)//2 
            count = 0
            for i in range(len(citations)):
                if citations[i]>= m:
                    count+=1

            if count >= m:
                ans = m 
                l = m + 1
            else:
                r = m - 1
        return ans
        