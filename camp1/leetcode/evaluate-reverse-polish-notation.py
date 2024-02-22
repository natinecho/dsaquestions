class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i=='+':
                a=st.pop()
                b=st.pop()
                st.append(a+b)
            elif i=='-':
                a=st.pop()
                b=st.pop()
                st.append(b-a)
            elif i=='/':
                a=st.pop()
                b=st.pop()
                st.append(int(b/a))
            elif i=='*':
                a=st.pop()
                b=st.pop()
                st.append(a*b)
            else:
                st.append(int(i))


        return st[0]

        