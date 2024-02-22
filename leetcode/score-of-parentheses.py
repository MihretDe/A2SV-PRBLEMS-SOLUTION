class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack  = []
        ans= 0
        for i in s:
            if i =='(':
                stack.append(i)
            else:
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    count = 0
                    while stack[-1] != '(':
                        count+=int(stack[-1])
                        stack.pop()
                    stack.pop()
                    stack.append(2*count)
                    # ans = 2*count
        # for i in stack:
        #     ans += int(i)
        # return ans
        return sum(stack)
                
                