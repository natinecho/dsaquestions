class RecentCounter:

    def __init__(self):
        self.dq=deque()
        self.tot=3000

    def ping(self, t: int) -> int:
        self.dq.append(t)
        temp=t-self.tot

        if temp<0:
            return len(self.dq)
            
        while self.dq and temp>self.dq[0]:
            self.dq.popleft()
        
        return len(self.dq)
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)