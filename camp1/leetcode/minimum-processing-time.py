class Solution:
    def minProcessingTime(self, pt: List[int], tasks: List[int]) -> int:
        pt.sort()
        tasks.sort(reverse = True)

        res = 0

        for i in range(len(pt)):
            temp = i*4
            maxx=0
            for j in range(temp,temp+5):
                maxx=max(pt[i]+tasks[temp],maxx)
            res = max(maxx,res)

        return res





        