class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float("inf")]*n
        dp[src]  = 0

        for i in range(k + 1):
            curr = dp[::]
            print(curr)

            for u,v,w in flights:
                curr[v] = min(curr[v],dp[u] + w)
            
            dp = curr[::]
        
        return dp[dst] if dp[dst] != float("inf") else -1
