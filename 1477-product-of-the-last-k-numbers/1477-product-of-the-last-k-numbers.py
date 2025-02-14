class ProductOfNumbers:

    def __init__(self):
        self.psum = []
        

    def add(self, num: int) -> None:
        self.psum.append(num)
        

    def getProduct(self, k: int) -> int:
        tot = 1
        for val in self.psum[-k:]:
            tot *= val

        return tot
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)