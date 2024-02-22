class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        slow,fast=0,0
        li=list(s)
        while fast<len(s):
            slow=fast+k
            li[fast:slow] = li[fast:slow][::-1]
            fast=min(fast+(2*k),len(li))
        return "".join(li)


