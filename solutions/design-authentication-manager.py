class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.val=timeToLive
        self.arr=defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.arr[tokenId] = self.val + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.arr[tokenId] > currentTime:
            self.arr[tokenId] = currentTime + self.val

        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for time in self.arr.values():
            if time > currentTime:
                count += 1
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)