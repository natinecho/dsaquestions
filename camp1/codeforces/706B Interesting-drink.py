import bisect
num = int(input())
arr = list(map(int,input().split()))

n = int(input())
arr.sort()
for i in range(n):

    val = int(input())

    print(bisect.bisect_right(arr,val))
    