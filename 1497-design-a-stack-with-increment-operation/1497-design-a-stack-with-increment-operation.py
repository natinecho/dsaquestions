class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.lenn = 0
        self.inc = [0]*maxSize
        self.maxx = maxSize

    def push(self, x: int) -> None:
        if self.lenn < self.maxx:
            self.arr.append(x)
            self.lenn += 1

    def pop(self) -> int:
        if self.lenn == 0:
            return -1

        self.lenn -= 1
        val = self.arr.pop() + self.inc[self.lenn]

        if self.lenn > 0:
            self.inc[self.lenn - 1] += self.inc[self.lenn] 

        self.inc[self.lenn]  = 0
        return val

    def increment(self, k: int, val: int) -> None:
        t = min(self.lenn,k)
        if self.lenn > 0:
            self.inc[t - 1] += val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)