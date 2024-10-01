class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [[float('inf')] * (k + 2) for _ in range(n)]
        
        for i in range(k + 2):
            dp[src][i] = 0
        
        for s in range(1, k + 2):
            for u, v, price in flights:
                dp[v][s] = min(dp[v][s], dp[u][s - 1] + price)
        
        result = min(dp[dst][s] for s in range(1, k + 2))
        
        return -1 if result == float('inf') else result