class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []

        maxx = 0
        val = 0
        for i in s:
            if i == ")":
                vv = 0
                while st and str(st[-1]).isdigit():
                   vv += st.pop()

                if st and st[-1] == "(":
                    st.pop()
                    st.append(vv + 1)
                else:
                    st.append(vv)
                    st.append(i)

                
            else :
                st.append(i)


        maxx = 0
        temp = 0

        for val in st:
            if str(val).isdigit():
                temp += val
            else:
                maxx = max(temp,maxx)
                temp = 0

        


        return 2*max(temp,maxx)


"""
)(()())())()(()()((((
0)4)1(2((((

"""
        