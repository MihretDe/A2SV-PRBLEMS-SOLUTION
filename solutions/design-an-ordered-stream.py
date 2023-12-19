class OrderedStream:

    def __init__(self, n: int):
        self.count = 1
        self.array = [0] *(n+2)
    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey] = value
        if self.count == idKey:
            while self.array[self.count] is not 0:
                self.count += 1
            return self.array[idKey:self.count]
        return []
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)