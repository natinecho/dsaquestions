class MinStack:

    # keep track of the miminum nuber until now in the stack
    def __init__(self):
        self.st = []
        # self.minn = float("inf")

    def push(self, val: int) -> None:
        self.st.append([val,min(val,self.st[-1][1] if self.st else float("inf"))])
        
    def pop(self) -> None:
        return self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0]
        
    def getMin(self) -> int:
        return self.st[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()