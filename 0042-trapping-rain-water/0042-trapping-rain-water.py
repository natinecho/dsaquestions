class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        ans = 0

        for i in range(len(height)):
            while st and st[-1][0] <= height[i]:
                hie,pos = st.pop()

                if st:
                    ans += (min(height[i], st[-1][0]) - hie) * (i - st[-1][-1] - 1)
            
            st.append((height[i], i))

        return ans


            

