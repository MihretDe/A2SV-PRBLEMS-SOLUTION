class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        occur = dict((a,i) for i,a in enumerate(s))
        l = 0
        r = 0
        ans = []
        for i in range(len(s)):
            if occur[s[i]] > r:
                r = occur[s[i]]
            if i == r:
                ans.append(r - l +1)
                l = r+1
        return ans 