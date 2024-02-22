class Solution:
    def simplifyPath(self, path: str) -> str:
        li=path.split('/')
        st=[]
        for i in li:
            if i == '..':
                if st:
                    st.pop()
            elif i and i != '.':
                st.append(i)

        return '/' + '/'.join(st)




        