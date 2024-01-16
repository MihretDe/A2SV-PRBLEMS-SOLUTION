class Solution:
    def balancedString(self, s: str) -> int:
        count = {'Q': 0, 'W': 0, 'R': 0, 'E': 0}
        for ch in s:
            count[ch] += 1

        target = len(s) // 4
        if all(count[ch] == target for ch in count):
            return 0
        window = {'Q': 0, 'W': 0, 'R': 0, 'E': 0}
        right = 0
        left = 0
        leng = float('inf')
        while right < len(s):
            window[s[right]] += 1
            while all(abs(window[char] - count[char]) <= target for char in count) and left <= right:
                leng = min(leng, right - left + 1)
                window[s[left]] -= 1
                left += 1
            right += 1

        return leng
        