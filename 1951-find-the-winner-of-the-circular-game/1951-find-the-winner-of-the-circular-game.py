class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n + 1)] 
        i = 0 
        while len(players) > 1:
            i = (i + k - 1) % len(players) 
            players.pop(i)
        return players[0] 