class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = [] 
        temp = k

        def back(ss):
            nonlocal k
            if len(ss) == n:
                ans.append(ss[::])
                k -= 1
                return 

            for i in range(3):
                if k<= 0:
                    return 
                if not ss or ord(ss[-1]) - 97 != i:
                    ss.append(chr(97 + i))
                    back(ss)
                    ss.pop()

            return 

        back([])

        

        return "".join(ans[-1]) if len(ans) == temp else ""
        