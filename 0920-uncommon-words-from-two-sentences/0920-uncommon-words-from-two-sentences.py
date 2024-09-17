class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ss = s1.split()
        ss.extend( s2.split())

        counter = Counter(ss)

        ans = []

        for word in counter:
            if counter[word] == 1:
                ans.append(word)

        return ans

