class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        bits = [0]*32

        for num in candidates:

            for i in range(32):
                if num & (1<<i):
                    bits[i]  += 1
        

        return max(bits)
        