class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for i in s:
            if i.isalnum():
                res+=i
        res=res.lower()
        return res==res[::-1]
