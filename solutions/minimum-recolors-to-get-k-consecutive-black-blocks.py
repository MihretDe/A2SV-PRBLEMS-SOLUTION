class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        countW = 0
        for i in range(k):
            if blocks[i] == "W":
                countW += 1
        left = 0
        right = k
        min_op = countW
        while right < len (blocks):
            if blocks[left] == 'W':
                countW -= 1
            if blocks[right] == "W":
                countW += 1
            min_op = min (min_op , countW)
            left+=1
            right+=1
        return min_op