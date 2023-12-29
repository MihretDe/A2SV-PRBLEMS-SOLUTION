class Solution:
    def sortSentence(self, s: str) -> str:
        words=s.split()
        res=[None]*len(words)
        for word in words:
            index=int(word[-1]) -1
            res[index]=word[:-1]
        # res = [word for word in res if word is not None]
        return " ".join(res)
