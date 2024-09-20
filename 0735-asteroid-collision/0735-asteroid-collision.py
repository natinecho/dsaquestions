class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for i in asteroids:
            if i < 0:
                flag = False
                while st and st[-1] > 0 and abs(i) >= st[-1]:
                    val = st.pop()
                    if val == abs(i):
                        flag = True
                        break
                    
                if not flag and (not st or st[-1] < 0):
                    st.append(i) 
            else:
                st.append(i)
        return st
