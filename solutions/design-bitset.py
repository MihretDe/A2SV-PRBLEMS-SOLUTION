class Bitset:

    def __init__(self, size: int):
        self.set_1 = set()
        self.set_0 = set(range(size))
        self.res=["0"]*size

    def fix(self, idx: int) -> None:
        self.set_1.add(idx)
        if idx in self.set_0:
            self.set_0.remove(idx)

    def unfix(self, idx: int) -> None:
        self.set_0.add(idx)
        if idx in self.set_1:
            self.set_1.remove(idx)
        

    def flip(self) -> None:
        temp = self.set_1
        self.set_1 = self.set_0
        self.set_0 = temp
        
    def all(self) -> bool:
        return len(self.set_0) == 0
    def one(self) -> bool:
        return len(self.set_1) != 0

    def count(self) -> int:
         return len(self.set_1)

    def toString(self) -> str:
        for i in self.set_1:
            self.res[i] = "1"
        for i in self.set_0:
            self.res[i] = "0"
        return ''.join(self.res)
        
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()