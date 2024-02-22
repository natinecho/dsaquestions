class Solution:
    def scoreOfParentheses(self, s: str) -> int:   
        res=[]
        for i in s:
            if i=='(':
                res.append(i)
            elif i==')' and res[-1]=='(':
                res[-1]=1
            else:
                score=0
                while res and res[-1]!='(':
                    score+=res.pop()

                res[-1]=score*2
            
        return sum(res)
                

            

                

                
                
                

        