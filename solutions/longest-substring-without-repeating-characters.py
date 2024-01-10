class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        words = set()
        length = 0
        if len(s) ==1:
            return 1
        while right < len(s):
            if s[right] not in words:
                words.add(s[right])
                length = max(length , len(words))
                right += 1
            else:
                length = max(length , len(words))
                words.remove(s[left])
                left +=1
               
        return length
