class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        ans = 0

        def back(seen, ind,count):
            nonlocal ans

            if ind == len(s):
                ans = max(ans,count)
                return 

            for i in range(ind + 1, len(s) + 1):
                if s[ind:i] not in seen:
                    seen.add(s[ind:i])
                    back(seen,i,count + 1)
                    seen.remove(s[ind:i])

            return 
        
        back(set(),0,0)

        return ans
        