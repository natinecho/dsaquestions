class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        prev = 0

        ans = []

        for i in spaces:
            ans.append(s[prev:i])
            prev = i

        ans.append(s[prev:])

        return " ".join(ans)
        