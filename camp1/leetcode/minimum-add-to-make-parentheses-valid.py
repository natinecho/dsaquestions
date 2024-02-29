class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s)==0:
            return 0
        ans=0
        st=[]

        for i in s:
            if i=='(':
                st.append(i)
            elif st and i==')':
                st.pop()
            else:
                ans+=1
        ans+=len(st)
        return ans
        