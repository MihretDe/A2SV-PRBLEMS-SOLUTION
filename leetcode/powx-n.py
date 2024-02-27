class Solution:
    def myPow(self, x: float, n: int) -> float:

        def solution(x: float, n: int):
            if n == 0:
                return 1
            z = n//2
            if n%2:
                res = solution(x , abs(z)) 
                return res * res * x
            else:
                res = solution(x , abs(z)) 
                return res * res
        result = solution(x,abs(n))
        if n < 0:
            return 1 / result
        return result 