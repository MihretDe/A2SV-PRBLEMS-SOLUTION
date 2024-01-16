class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        right = 0
        max_count = 0
        length = 0

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            length = max(length, right - left + 1)
            right += 1

        return length

