class Solution:
    def pivotInteger(self, n: int) -> int:
        num = list(i for i in range(1,n+1))

        psum = 0
        summ = sum(num)

        for i in range(len(num)):
            if psum == summ -( psum + num[i]):
                return num[i]
            psum += num[i]
        return -1