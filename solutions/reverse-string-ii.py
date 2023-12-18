class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reversed_word = []
        for i in range(0, len(s), k):
            sliced = s[i:i+k]
            if i // k % 2 == 0:
                reversed_word.append(sliced[::-1])
            else:
                reversed_word.append(sliced)
        return "".join(reversed_word)





            
        