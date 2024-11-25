class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        tot_factory = []

        for pos,lim in factory:
            for i in range(lim):
                tot_factory.append(pos)

        n = len(tot_factory)
        dp = [0]*(n + 1)
        

        for i in range(len(robot) - 1,-1,-1):
            curr = [0]*(n + 1)
            curr[-1] = float("inf")

            for j in range(n - 1,-1,-1):

                take = abs(robot[i] - tot_factory[j]) + dp[j + 1]

                leave = curr[j + 1]

                curr[j] = min(leave , take)

            dp = curr[::]

        
        return dp[0]

