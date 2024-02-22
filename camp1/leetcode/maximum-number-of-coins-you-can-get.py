class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        coins=0
        i=0
        print(piles)
        while i<len(piles):
            i+=2
            coins+=piles[i-1]
            piles.pop()
        return coins
        