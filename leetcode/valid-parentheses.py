class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for l in s:
            if stack and l==')' and stack[-1]=='(':
                stack.pop()
            elif stack and l==']' and stack[-1]=='[':
                stack.pop()
            elif stack and l=='}' and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(l)
        if not stack :
            return True
        else:
            return False
