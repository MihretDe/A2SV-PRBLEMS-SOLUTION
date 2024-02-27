class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        stack2  = []
        num = []
        l =0
        while l < len(s):
            if s[l] >= '0' and s[l]<='9':
                while s[l] >= '0' and s[l]<='9':
                    num.append(s[l])
                    l+=1
                l-=1
                stack.append(int(''.join(num)))
                num = [] 
            elif s[l] == ']':
                curr = []
                while stack[-1] != '[':
                    curr.append(stack.pop())
                curr.reverse()
                stack.pop()
                n= int(stack.pop())
                ans = ''.join(curr) * n
                stack.append(ans)
            else:
                stack.append(s[l])
            l+=1
        return ''.join(stack)


                    

        