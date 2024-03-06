class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solution(n:int , k : int):
            if n==1:
                return 0
            prev=solution(n-1 , ceil(k/2))
            if prev==0 and k%2==0 or (prev==1 and k%2):
                return 1
            else:
                return 0

        return solution(n,k)

        