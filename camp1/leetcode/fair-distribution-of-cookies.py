class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        ans = [0]*k
        minn = float("inf")

        def backTrack(i):
            nonlocal minn
            if i == len(cookies):
                minn = min(minn,max(ans))
                return 
            
            for  j in range(k):
                ans[j] += cookies[i]

                if ans[j]<minn:
                    backTrack(i+1)

                ans[j] -= cookies[i]
        
        backTrack(0)

        return minn

        