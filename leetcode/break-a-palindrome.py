class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        list_word = list(palindrome)
        found = False
        for i in range(len(palindrome)):
            if len(palindrome) % 2 ==1 and i == len(palindrome)//2:
                continue
                
            else:
                if list_word[i] != 'a':
                    list_word[i]='a'
                    found = True
                    break
        if found:
            return ''.join(list_word)
        list_word[-1] ='b'
        return ''.join(list_word) 

