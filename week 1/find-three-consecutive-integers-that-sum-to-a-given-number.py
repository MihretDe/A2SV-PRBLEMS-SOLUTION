class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3!=0:
            return[]
        else:
            y=num//3
            return [y-1,y,y+1]
        
        