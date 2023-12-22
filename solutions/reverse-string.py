class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
          s[i], s[-i - 1] = s[-i - 1], s[i]
        # front = 0
        # end = len(s) - 1
        # while front < end:
        #     s[front], s[end] = s[end], s[front]
        #     front += 1
        #     end -= 1
        