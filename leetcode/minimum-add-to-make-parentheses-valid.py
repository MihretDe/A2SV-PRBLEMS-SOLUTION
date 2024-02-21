class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        var =0
        ans =0
        for i in range(len(s)):
            if s[i] == '(':
                var +=1
            else:
                if var ==0:
                    ans+=1
                else:
                    var-=1
        return ans+var
