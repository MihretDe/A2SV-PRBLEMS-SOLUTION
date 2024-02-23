class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack =[]
        counter  = Counter(s)
        for i in s:
            while stack and counter[stack[-1]]>0 and stack[-1] >i and (i not in stack):
                print(stack.pop())
            if i not in stack:
                stack.append(i)
            counter[i]-=1
        return "".join(stack)