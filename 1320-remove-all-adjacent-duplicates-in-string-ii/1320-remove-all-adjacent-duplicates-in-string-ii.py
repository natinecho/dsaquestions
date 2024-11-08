class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        st = []

        for i in s:
            if st and st[-1][0] == i: 
                if st[-1][1] < k - 1:
                    st[-1][1] += 1
                else:
                    st.pop()
            else:
                st.append([i,1])
        
        ans = ""

        for val in st:
            ans += (val[0]*val[1])
    
        return ans
            
        