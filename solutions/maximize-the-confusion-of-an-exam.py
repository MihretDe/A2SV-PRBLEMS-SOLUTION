class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        countT = 0
        countF = 0
        length = 0
        for i in range(len(answerKey)):
            if answerKey[i] == 'T':
                countT += 1
            else:
                countF += 1
            while countT > k and countF > k and left < len(answerKey):
                if answerKey[left] == 'T':
                    countT -= 1
                else:
                    countF -= 1
                left +=1
            length = max(length , i - left + 1)
        return length 
