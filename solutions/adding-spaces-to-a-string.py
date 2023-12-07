class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        modifiedString = []
        lastIndex = 0
        for index in spaces:
            modifiedString.append(s[lastIndex:index] + " ")
            lastIndex = index
        modifiedString.append(s[lastIndex:])
        return "".join(modifiedString)
          
        

        