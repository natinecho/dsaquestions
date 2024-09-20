class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        intervals.sort()

        st = []

        for start,end in intervals:

            while st and st[-1][0] <= start <= st[-1][1]:
                ss,ee = st.pop()

                start = min(ss,start)
                end = max(ee,end)

            st.append([start,end])


        return st