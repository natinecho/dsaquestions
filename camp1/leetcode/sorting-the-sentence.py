class Solution:
    def sortSentence(self, s: str) -> str:
        d={}
        li=s.split()
        li.sort(key=lambda x:x[-1])
        m=[]
        for i in li:
            m.append(i[:-1])
        res=' '.join(m)

        return res
        