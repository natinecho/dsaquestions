class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        psum = [0]*(pow(10,6) + 1)

        for st,en in intervals:
            psum[st] += 1
            psum[en + 1] -= 1

        for i in range(len(psum)):
            psum[i] += psum[i -1]
        

        return max(psum)


        