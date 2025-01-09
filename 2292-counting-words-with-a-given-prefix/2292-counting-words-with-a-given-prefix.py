class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cc = 0

        for word in words:
            if len(pref) <= len(word) and word[:len(pref)] == pref:
                cc += 1

        return cc
        