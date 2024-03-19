class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = []
        def generate(open , close):
            if open == close == n:
                ans.append(''.join(temp))
                return
            if open < n:
                temp.append('(')
                generate(open + 1 , close)
                temp.pop()
            if close < open:
                temp.append(')')
                generate(open , close + 1)
                temp.pop()
        generate (0 , 0)
        return ans
