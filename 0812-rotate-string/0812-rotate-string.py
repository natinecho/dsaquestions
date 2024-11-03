class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)

        if len(goal) != n:
            return False

        for i in range(n):
            if s[i:] == goal[:n - i] and s[:i] == goal[n - i:]:
                return True

        return False
        