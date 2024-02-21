class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c=Counter(answers)
        sets=set(answers)
        ans=0
        for i in sets:
            if i==0:
                ans+=c[i]
            elif c[i]<=(i+1):
                ans+=(i+1)
            else:
                while c[i]>i:
                    ans+=(i+1)
                    c[i]-=(i+1)
                
                if c[i]>0:
                    ans+=(i+1)
             
        return ans

        