class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:

        res = [0]*len(flips)
        count=0
        maxx=0
        summ=0
        psum=0

        for i in range(len(flips)):

            maxx=max(maxx,flips[i]-1)
            if flips[i]-1<=maxx:
                psum+=1
            res[flips[i]-1]=1
            summ+=1
            if psum==maxx+1:
                count+=1

        return count


        