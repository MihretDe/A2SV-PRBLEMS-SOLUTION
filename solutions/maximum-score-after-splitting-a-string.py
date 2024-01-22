class Solution:
    def maxScore(self, s: str) -> int:
        prefix = []
        if s[0] == '0':
            prefix.append(1)
        else:
            prefix.append(0)
        for i in range(1, len(s)):
            if s[i] == '0':
                prefix.append(prefix[i-1] + 1)
            else:
                prefix.append(prefix[i-1] )
           
        suffix = [int(s[-1])]
        i =1
        for j in range(len(s) -2 , -1 , -1):
            suffix.append(suffix[i-1] + int(s[j]))
            i+=1
        suffix.reverse()
        max_score = float('-inf')
        for i in range(len(prefix)-1):
            max_score = max(max_score , prefix[i] + suffix[i+1])
        return max_score
        