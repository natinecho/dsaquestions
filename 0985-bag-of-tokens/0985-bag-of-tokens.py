class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res = 0

        l = 0
        r = len(tokens) -1

        while l <= r:
            if power >= tokens[l]:
                res += 1
                power -= tokens[l]
                l += 1

            elif res >= 1 and r - 1 > l:
                res -= 1
                power += tokens[r]
                r -= 1
            else:
                break

            
        return res



        