class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ","")
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        l=0
        r=len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False
            r-=1
            l+=1
        return True