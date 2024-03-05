class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        
        def divide(l,r):
            nonlocal ans
            temp = set(s[l:r])
            f=0
            i=0
            for i in range(l,r):

                if s[i].isupper() and s[i].lower() not in temp:
                    f=1
                    break
                elif s[i].islower() and s[i].upper() not in temp:
                    f=1
                    break
            if f==1:
                divide(l,i)
                divide(i+1,r)

            if f ==0 and r-l>1:
                if len(ans)<r-l:
                    ans = s[l:r]                  
                    

        divide(0,len(s))
        print(ans)

        return ans
