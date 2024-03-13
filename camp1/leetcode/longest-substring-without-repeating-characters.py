class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        sets = set()
        l = r = 0
        while r < len(s):
            if s[r] in sets:
                maxx = max(maxx,len(sets))
                sets.remove(s[l])
                l+= 1
            else:
                sets.add(s[r])
                r += 1
        return max(maxx, len(sets))