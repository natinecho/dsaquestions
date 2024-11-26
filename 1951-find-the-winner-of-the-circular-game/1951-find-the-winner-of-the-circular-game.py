class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q=deque(i for i in range(1,n+1))
        count=0

        k %= n

        if k == 0:
            k = n
        while len(q)>1:
            count+=1
            if count!=k:
                q.append(q.popleft())
            else:
                q.popleft()
                count=0
            
        return q[-1]
