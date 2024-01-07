class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        else:
            left = 0
            right = 0
            while left < len(name) and right < len(typed):
                if name[left] == typed[right]:
                    count = 0
                    while left < len(name) - 1 and name[left] == name[left + 1]:
                        left += 1
                        count += 1
                    countT = 0
                    while right < len(typed) - 1 and typed[right] == typed[right + 1]:
                        right += 1
                        countT += 1
                    if count > countT:
                        return False
                else:
                    return False
                left += 1
                right += 1
            if left < len(name) or right < len(typed):
                return False
        return True




       


                    