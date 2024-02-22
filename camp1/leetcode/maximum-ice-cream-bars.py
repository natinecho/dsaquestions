class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i=0
        count=0
        while coins>0 and i<len(costs):
            if costs[i]>coins:
                return count
            coins-=costs[i]
            i+=1
            count+=1
        return count
            

        