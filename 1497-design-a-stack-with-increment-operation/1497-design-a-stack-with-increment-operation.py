class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.lenn = 0
        self.maxx = maxSize

    def push(self, x: int) -> None:
        if self.lenn < self.maxx:
            self.arr.append(x)
            self.lenn += 1


    def pop(self) -> int:
        if self.lenn > 0:
            self.lenn -= 1
            return self.arr.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k,len(self.arr))):
            self.arr[i] += val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)