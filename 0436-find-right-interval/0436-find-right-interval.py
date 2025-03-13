class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        st = []
        ed = []

        for i in range(len(intervals)):
            st.append((intervals[i][0],i))
            ed.append((intervals[i][1],i))

        st.sort()
        ed.sort()

        i = 0
        j = 0

        ans = [-1] * len(intervals)

        while i < len(st) and j < len(ed):
            if ed[j][0] <= st[i][0]:
                ans[ed[j][1]] = st[i][1]
                j += 1 

            else:
                i += 1


        return ans























        # st = []
        # ans = []

        # for i in range(len(intervals)):
        #     st.append(intervals[i][0])

        # temp = st[:]
        # st.sort()

        # for i in range(len(intervals)):
        #     key = intervals[i][1]
        #     l = 0 
        #     r = len(st)-1
        #     num = -1

        #     while l<=r:
        #         m = (l+r)//2
        #         if  st[m] >= key:       
        #             num = temp.index(st[m])
        #             r = m - 1
        #         elif st[m] < key:
        #             l = m + 1

        #     ans.append(num)
            
        # return ans
