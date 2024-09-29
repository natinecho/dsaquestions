class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split(" ")
        strr=[]
        for i in arr:
             strr.append(i[::-1])
        return " ".join(strr)
        