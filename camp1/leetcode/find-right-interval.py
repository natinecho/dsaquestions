class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        st = []
        ans = []

        for i in range(len(intervals)):
            st.append(intervals[i][0])

        temp = st[:]
        st.sort()

        for i in range(len(intervals)):
            key = intervals[i][1]
            l = 0 
            r = len(st)-1
            num = -1

            while l<=r:
                m = (l+r)//2
                if  st[m] >= key:       
                    num = temp.index(st[m])
                    r = m - 1
                elif st[m] < key:
                    l = m + 1

            ans.append(num)
            
        return ans
