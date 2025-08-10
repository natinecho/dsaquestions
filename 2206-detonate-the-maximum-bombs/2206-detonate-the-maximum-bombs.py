class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def dfs(i):
            st = [i]
            sets = set([i])
            ans = 0
            while st:
                node = st.pop()
                x,y,r = bombs[node]
                ans += 1

                for i in range(len(bombs)):
                    if i not in sets:
                        x2,y2,r2 = bombs[i]
                        dis = sqrt(pow(abs(x2 - x),2) + pow(abs(y2 - y),2))

                        if dis <= r:
                            st.append(i)
                            sets.add(i)

            return ans

       

        _max = 0
        for i in range(len(bombs)):
            _max = max(_max,dfs(i))
        

        return _max

        