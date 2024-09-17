class Solution:
    def monkeyMove(self, n: int) -> int:
        return (pow(2,n,(pow(10,9) + 7)) - 2) % (pow(10,9) + 7)