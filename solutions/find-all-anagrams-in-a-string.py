class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        target = Counter(p)
        window = Counter(s[0:len(p)])
        if window == target:
            ans.append(0)
        left = 0
        right=len(p)
        while right < len(s):
            window[s[left]] -= 1
            window[s[right]] = window.get(s[right] , 0) + 1
            if  window[s[left]] ==0:
                del window[s[left]]
            left+= 1
            if window == target:
                ans.append(left)
            
            right += 1
        return ans
