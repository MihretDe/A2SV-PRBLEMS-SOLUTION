class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=min(len(word1),len(word2))
        out=""
        for i in range(l):
            out+=word1[i]
            out+=word2[i]
            i+=1
        if l<len(word1):
            out+=word1[l:]
        elif l<len(word2):
            out+=word2[l:]
        return out


        