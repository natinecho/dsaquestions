class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        temp = [(positions[i],healths[i],directions[i],i) for i in range(len(healths))]
        temp.sort()

        st = []

        for position,health,direction,index in temp:

            if direction == "L":
                flag = False

                while st and st[-1][1] <= health and direction  != st[-1][2]:
                    pos,hel,di,ind = st.pop()
                    if  hel == health:
                        flag = True
                        break

                    health -= 1

            
                if not flag and (not st or direction  == st[-1][2]):
                    st.append((position,health,direction,index))

                elif not flag and  st and st[-1][1] > health:
                    pos,hel,di,ind = st.pop()
                    st.append((pos,hel - 1,di,ind))
                # else:

            else:
                st.append((position,health,direction,index))

            
        st.sort(key = lambda x: x[3])

        ans = []

        for p,h,d,i in st:
            ans.append(h)

        

        return ans
        