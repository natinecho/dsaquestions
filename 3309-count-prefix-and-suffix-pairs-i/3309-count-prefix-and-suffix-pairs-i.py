class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        ans = 0

        for i in range(len(words)- 1):
            nn = len(words[i])
            for j in range(i + 1,len(words)):
                if nn <= len(words[j]) and words[i] == words[j][:nn] == words[j][len(words[j]) - nn:]:
                    ans += 1


        return ans
        