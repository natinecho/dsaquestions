class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        st = []
        ed = []

        for i in range(len(intervals)):
            st.append((intervals[i][0], i))
            ed.append((intervals[i][1], i))

        st.sort()
        ed.sort()

        ans = [-1] * (len(intervals))

        i = 0
        j = 0

        while i < len(ed) and j < len(st):

            if ed[i][0] <= st[j][0]:
                ans[ed[i][1]] = st[j][1]
                i += 1
            else:
                j += 1


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
