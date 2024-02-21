class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x:x[1])
        num=points[0][1]
        arrow=1
        for i in points:
            if num<i[0]:
                num=i[1]
                arrow+=1
        return arrow



        