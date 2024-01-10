class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a','e', 'i' , 'o' , 'u']
        count =0
        for i in range(k):
            if s[i] in vowel:
                count += 1
        left = 0
        right = k
        max_count = count
        while right < len(s):
            if s[left] in vowel:
                count -= 1
            left += 1
            if s [right] in vowel:
                count += 1
            max_count = max(max_count , count)
            right += 1
        return max_count