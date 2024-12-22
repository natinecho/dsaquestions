class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a == b:
                ans[i] = a
            elif heights[max(a, b)] > heights[min(a, b)]:
                ans[i] = max(a, b)

        arr = []
        for i, (a, b) in enumerate(queries):
            if ans[i] == -1:
                arr.append((max(a, b), max(heights[a], heights[b]), i))

        queries = sorted(arr, key=lambda x: x[0] , reverse = True)
        st = []
        
        for end, maxx, idx in queries:
            while end + 1 < len(heights):

                val = heights.pop()
                while st and -st[-1][0] <= val:
                    st.pop()
                    
                st.append((-val, len(heights)))

            res = bisect_left(st, (-maxx, -1)) - 1
            if res >= 0:
                ans[idx] = st[res][1]
        return ans        