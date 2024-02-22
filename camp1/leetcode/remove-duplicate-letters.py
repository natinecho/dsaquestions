class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c=Counter(s)
        st=[]
        sets=set()
        for i in s:
            if i in sets:
                c[i]-=1
                continue
            if not st:
                st.append(i)
                sets.add(i)
                c[i]-=1
                continue
            while st and st[-1]>i and c[st[-1]]>0:
                sets.remove(st.pop())
            st.append(i)
            sets.add(i)
            c[i]-=1
        return ''.join(st)


        