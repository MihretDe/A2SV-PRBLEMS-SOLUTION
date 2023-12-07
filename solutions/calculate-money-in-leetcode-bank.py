class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7:
            return sum(range(1, n+1)) 
        full = n//7
        remain = n%7
        summoney = 0
        last_monday=1
        for i in range(1,full+1):
            summoney += sum(range(i,i+7))
            last_monday += 1
        if remain > 0:
            summoney += sum(range(last_monday,last_monday+remain))
        return summoney
