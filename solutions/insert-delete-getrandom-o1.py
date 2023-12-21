class RandomizedSet:

    def __init__(self):
        self.randomlist=[]
        self.randomdict={}
        self.count = 0
    def insert(self, val: int) -> bool:
        if val not in self.randomdict:
            self.randomlist.append(val)
            self.randomdict[val] = self.count
            self.count += 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        if val in self.randomdict:
            i = self.randomdict[val]
            self.randomlist[i], self.randomlist[-1] = self.randomlist[-1], self.randomlist[i]
            self.randomlist.pop()
            if i < len(self.randomlist):
                self.randomdict[self.randomlist[i]] = i  
            del self.randomdict[val]
            self.count -= 1
            return True
        else:
            return False

        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.randomlist) - 1)
        return self.randomlist[index]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()