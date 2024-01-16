class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * len(s)

        for shift in shifts:
            if shift[2] == 0:
                prefix[shift[0]] -= 1
                if shift[1] != len(s) - 1:
                    prefix[shift[1] + 1] += 1
            else:
                prefix[shift[0]] += 1
                if shift[1] != len(s) - 1:
                    prefix[shift[1] + 1] -= 1

        for i in range(1, len(s)):
            prefix[i] += prefix[i - 1]

        ans = []
        for i in range(len(s)):
            curr = ord(s[i]) + prefix[i] %26
            if curr > 122:
                curr = (curr - 97) % 26 + 97  
            elif curr < 97:
                curr = (curr - 122) % 26 + 122  
            ans.append(chr(curr))

        return "".join(ans)
