class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        wcount1 = Counter(words1)
        wcount2 = Counter(words2)

        for word in words1:
            if wcount1[word] == 1 and wcount2[word] == 1:
                count += 1

        return count
        