class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        s1 = ''
        length = len(s) - 1
        while length >= 0:
            s1 = s1 + s[length]
            length = length - 1
        if s == s1:
            return True
        return False