class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        n=len(temperatures)
        res=[0]*n
        for i in range(n):
            while st and temperatures[i]>temperatures[st[-1]]:
                temp=st.pop()
                res[temp]=i-temp
            st.append(i)
        return res


        