class Solution:
    def minimumSteps(self, s: str) -> int:
        count1 = 0
        ans = 0
        right = len(s) - 1
        while right >= 0:
            if s[right] == '0':
                count1 += 1
            else :
                ans += count1
            right-=1     
        return ans

        