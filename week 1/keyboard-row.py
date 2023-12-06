class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result=[]
        for word in words:
            count=0
            if word[0].lower() in "qwertyuiop":
                for char in word:
                    if char.lower() in "qwertyuiop":
                        count+=1
            elif word[0].lower() in "asdfghjkl":
                for char in word:
                    if char.lower() in "asdfghjkl":
                        count+=1
            elif word[0].lower() in "zxcvbnm":
                for char in word:
                    if char.lower() in "zxcvbnm":
                        count+=1
            if count == len(word):
                result.append(word)
                        

        return result

        