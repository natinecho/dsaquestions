class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        arr = sentence.split()
        n = len(searchWord)

        for i in  range(len(arr)):
            if len(arr[i]) >= n and searchWord == arr[i][:n]:
                return i + 1

        return -1