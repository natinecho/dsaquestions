class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        ternary = set()

        while n > 0:
            ternary.add(n % 3)
            n //= 3 

        return 2 not in ternary


        