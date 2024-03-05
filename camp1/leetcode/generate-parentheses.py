class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []
        
        def backTrack(s,op,cl):
            
            if op<n:
                s.append('(')
                backTrack(s,op+1,cl)
                s.pop()
            
            if cl<n and cl<op:
                s.append(')')
                backTrack(s,op,cl+1)
                s.pop()

            if cl == op == n:
                temp = "".join(s.copy())
                ans.append(temp)
                return
                 

        backTrack([],0,0)

        return ans


