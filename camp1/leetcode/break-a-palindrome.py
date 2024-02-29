class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        arr = list(palindrome)
        num=0
        if len(arr)%2==0:
            num=len(arr)//2
        elif len(arr)==1:
            return ''
        else:
            num=(len(arr)//2)

        for i in range(len(arr)):
            if arr[i]!='a' and not i==num:
                arr[i]='a'
                break
            if i==len(arr)-1:
                arr[i]='b'
                break
        return "".join(arr)
            

            



        