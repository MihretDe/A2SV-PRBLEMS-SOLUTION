class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        left=0
        right=0
        g.sort()
        s.sort()
        satisfied=0
        while right < len(s)and left<len(g):
            if g[left] <= s[right]:
                left+=1
                satisfied+=1
            right+=1
        return satisfied


