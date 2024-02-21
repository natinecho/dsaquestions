class Solution:
    def isHappy(self, n: int) -> bool:
        count=0
        while n>1:
            res=0
            while n>=1:
                rem=n%10
                res+=(rem**2)
                n=n//10
            count+=1
            n=res
            if count>1 and n<9 and n!=1:
                return False
        return True



        