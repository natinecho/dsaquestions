from itertools import accumulate

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(val, target, curr = 0, idx = 0):
            if idx == len(val):
                return curr == target
            
            num = 0
            for i in range(idx, len(val)):
                num = num * 10 + int(val[i])
                if check(val, target, curr + num, i + 1):
                    return True
            
            return False
        
        squares = [0]  
        for i in range(1, 1001):
            square = i * i
            if check(str(square), i,0,0):
                squares.append(square)
            else:
                squares.append(0)

        psum = list(accumulate(squares)) 
        return psum[n]
