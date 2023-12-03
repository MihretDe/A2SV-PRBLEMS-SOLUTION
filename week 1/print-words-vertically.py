class Solution:
    def printVertically(self, s: str) -> List[str]:
        ar = list(map(str, s.split()))
        max_length = max(ar, key=len)
        max_length_length = len(max_length)
        result = [""] * max_length_length 

        for i in range(max_length_length):
            re = ""
            for j in range(len(ar)):
                if i < len(ar[j]):
                    re += ar[j][i]
                else:
                    re += " "
            result[i] = re.rstrip()  

        return result