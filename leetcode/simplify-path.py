class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        # print(path_list)
        stack = []
        for p in path_list:
            if p == '..':
                if stack:
                    stack.pop()
            elif p!='.' and p!='':
                stack.append(p)
        # print(stack)
        ans = '/' + ('/').join(stack)
        return ans
         