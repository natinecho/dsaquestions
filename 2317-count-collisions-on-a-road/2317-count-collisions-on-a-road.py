class Solution:
    def countCollisions(self, directions: str) -> int:
        st = []
        count = 0
        curr = ""

        for di in directions:
            curr = di
            while st and curr != st[-1]:
                if st[-1] == "R" and curr == "L":
                    st.pop()
                    curr = "S"
                    count += 2

                elif st[-1] == "R" and curr == "S":
                    count += 1
                    st.pop()

                elif st[-1] == "S" and curr == "L":
                    st.pop()
                    curr = "S"
                    count += 1 
                else:
                    break
                


            st.append(curr)

        
        return count
            


        
