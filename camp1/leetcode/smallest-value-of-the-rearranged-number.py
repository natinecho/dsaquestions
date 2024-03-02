class Solution:
    def smallestNumber(self, num: int) -> int:
        n = abs(num)
        flag=0

        s = list(str(n)) 

        if num<0:
            s.sort(reverse = True)
            temp="".join(s)
            return int(temp)*-1
        elif len(s)==1:

            return int(s[0])

        else:
            s.sort()

            if s[0]=="0":
                for i in range(len(s)):
                    if s[i]!="0":
                        s[0],s[i]=s[i],s[0]
                        break

            temp="".join(s)
            n=int(temp)
             
        return n