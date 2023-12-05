class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        Sword1=''.join(word1)
        Sword2=''.join(word2)
        if Sword1==Sword2:
            return True
        return False
        