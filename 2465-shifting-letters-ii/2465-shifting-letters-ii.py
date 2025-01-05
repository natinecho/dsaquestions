class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = [0]*(len(s)+1)

        for i in range(len(shifts)):
            if shifts[i][2] == 0:
                temp[shifts[i][0]] -= 1
                temp[shifts[i][1] + 1] += 1
            else:
                temp[shifts[i][0]] += 1
                temp[shifts[i][1] + 1] -= 1
        
        ans = []
        psum = 0

        for i in range(len(temp)-1):
            psum += temp[i]
            ch = (ord(s[i]) + psum - 97 )% 26
            ans.append(chr(ch + 97))


        return "".join(ans)
            
        