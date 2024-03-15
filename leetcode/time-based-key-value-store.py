class TimeMap:

    def __init__(self):
        self.timestamp = defaultdict(list)
        self.value = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamp[key].append(timestamp)
        self.value[key].append(value)
    def get(self, key: str, timestamp: int) -> str:
        val = self.timestamp[key]
        ans = self.value[key]
        if not val or timestamp < val[0] :
            return ""
        k = bisect_left(val , timestamp)
        if k == len(val) or val[k] > timestamp  : k -=1
        return ans[k]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)