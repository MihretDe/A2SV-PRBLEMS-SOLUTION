class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for key , value in count.items():
            if value <= key+1:
                ans += key+1
            else:
                ans+= (key+1)*ceil(value / (key+1))
        return ans 

