class Solution:
    def maxScore(self, s: str) -> int:

        arr = list(map(int,s))
        ones = sum(arr)
        zeros = 0
        max_ = 0
        for i in range(0,len(arr)-1):
            if  arr[i] == 0 :
                zeros += 1
            else:
                ones -= 1
            max_ = max(max_, ones + zeros)

        return max_

        