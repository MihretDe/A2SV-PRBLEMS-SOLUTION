class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        window = Counter(s2[:len(s1)])

        if target == window:
            return True

        left = 0
        right = len(s1)

        while right < len(s2):
            window[s2[left]] -= 1
            
            window[s2[right]] = window.get(s2[right], 0) + 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            if target == window:
                return True
            
            left += 1
            right += 1

        return False

