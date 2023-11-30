class Solution:
    def interpret(self, command: str) -> str:
        out=""
        temp=""
        for char in command:
            if char=='G':
                out+='G'
            else:
                temp+=char
                if temp=="()":
                    out+='o'
                    temp=""
                elif temp=="(al)":
                   out+='al'
                   temp=""
        return out

        