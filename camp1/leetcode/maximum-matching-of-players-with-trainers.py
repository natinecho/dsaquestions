class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l,r=0,0
        matches=0
        while l<len(players) and r<len(trainers):
            if players[l]<=trainers[r]:
                  l+=1
                  r+=1
                  matches+=1
            else:
                r+=1
        return matches

        
        