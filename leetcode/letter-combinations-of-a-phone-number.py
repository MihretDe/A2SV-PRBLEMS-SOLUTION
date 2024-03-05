class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        count = {2:['a' ,'b','c'] , 3 :['d','e','f'] ,4:['g' ,'h','i'] ,5:['j','k','l'] ,6:['m','n','o'],7:['p','q','r','s'], 8:['t','u','v'],9:['w','x','y','z'] }
        
        def combine(x , path):
            if len(path) == len(digits):
                ans.append(''.join(path[:]))
                return
            if x >= len(digits):
                return
            for i in range(len(count[int(digits[x])])):
                path.append(count[int(digits[x])][i])
                combine(x+1 , path)
                path.pop()
        if digits == "":
            return []

        combine ( 0 , [])
        return ans
