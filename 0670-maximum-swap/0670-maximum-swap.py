class Solution:
    def maximumSwap(self, num: int) -> int:
        maxx = num
        ss = list(str(num))


        for i in range(len(ss)):
            for j in range(i + 1,len(ss)):
                ss[i],ss[j] = ss[j],ss[i]
                maxx = max(maxx,int("".join(ss)))
                ss[i],ss[j] = ss[j],ss[i]

        return maxx


        