class Solution:
    def minimumDeletions(self, s: str) -> int:
    

        # def back(ind, is_b):
        #     if (ind,is_b) in dp:
        #         return dp[(ind,is_b)]
            
        #     if ind == len(s):
        #         return 0

        #     if s[ind] == "a":
        #         dp[(ind,is_b)] = (1 + back(ind + 1, is_b)) if is_b else back(ind + 1, is_b)
        #     elif s[ind] == "b" and is_b:
        #         dp[(ind,is_b)] = back(ind + 1, is_b)
        #     elif s[ind] == "b" and not is_b:
        #         dp[(ind,is_b)] = min(1 + back(ind + 1, is_b),back(ind + 1, not is_b))

        #     return dp[(ind,is_b)]

        # dp = {}
        # return back(0,False)

        count = 0
        ans = 0

        for i in range(len(s)):
            if s[i] == "a":
                ans = min(ans + 1,count)
            else:
                count += 1

        return ans