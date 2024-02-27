class Solution:
    def decodeString(self, s: str) -> str:
        def decode(l,r):
            ans=""
            digit=""
            num=1
            start=-1
            openb=0
            for i in range(l,r):
                if s[i].isdigit():
                    digit+=s[i]
                elif s[i]=='[':
                    if openb==0:
                        num=int(digit)
                        start=i
                    openb+=1
                    digit=""
                elif s[i]==']':
                    openb-=1
                    if openb==0:
                        ans+=num*decode(start+1,i)
                elif openb==0:
                    ans+=s[i]
                    
            return ans

        return decode(0,len(s))








         
        