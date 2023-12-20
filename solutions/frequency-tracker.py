class FrequencyTracker:
    freq = {}
    def __init__(self):
        self.freq = defaultdict(int)
        self.freqvalue =defaultdict(int)

    def add(self, number: int) -> None:

        self.freq[number] += 1
        curr = self.freq[number]
        self.freqvalue[curr] += 1
        self.freqvalue[curr-1] -= 1
            

    def deleteOne(self, number: int) -> None: 
        if self.freq[number] > 0:
            self.freq[number] -= 1
            curr = self.freq[number]
            self.freqvalue[curr] += 1
            self.freqvalue[curr+1] -= 1


    def hasFrequency(self, frequency: int) -> bool: 
        return self.freqvalue[frequency] > 0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)