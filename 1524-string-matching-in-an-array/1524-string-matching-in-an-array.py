class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []

        for word in words:

            for ww in words:
                if word in ww and word != ww:
                    ans.append(word)
                    break


        return ans
            
        