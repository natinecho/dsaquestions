class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        maxx = 0
        for st,en in intervals:
            maxx = max(maxx,st,en)

        psum = [0]*(maxx + 2)

        for st,en in intervals:
            psum[st] += 1
            psum[en + 1] -= 1

        for i in range(1,len(psum)):
            psum[i] += psum[i - 1]
        

        return max(psum)


        