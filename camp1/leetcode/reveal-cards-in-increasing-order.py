class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        d=deque()
        ans=[0]*len(deck)    
        for i in range(len(deck)): 
            d.append(i)
        for i in range(len(deck)):
            if d:
                a=d.popleft()
                ans[a]=deck[i]
            if d:
                d.append(d.popleft())

        return ans