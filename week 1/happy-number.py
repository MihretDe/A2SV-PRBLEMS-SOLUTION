class Solution:
    def isHappy(self, n: int) -> bool:
        exists =set()
        if n == 1:
            return True
        while n != 1:
            str_n = str(n)
            n_sum = 0
            for i in range(len(str_n)):
                n_sum += int(str_n[i]) ** 2
            if n_sum in exists:
                break
            else:
                exists.add(n_sum)
            if n_sum == 1:
                return True
            n = n_sum
        return False


        