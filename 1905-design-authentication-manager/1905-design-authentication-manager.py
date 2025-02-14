class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.Tokens = {}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.Tokens[tokenId] = currentTime
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.Tokens and  currentTime - self.timeToLive < self.Tokens[tokenId]:
            self.Tokens[tokenId] = currentTime
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cc = 0
        for tt in self.Tokens:
            if  currentTime - self.timeToLive < self.Tokens[tt]:
                cc += 1

        return cc
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)