class Solution:
    def average(self, salary: List[int]) -> float:
        w=sorted(salary)
        sum=0
        for i in range(1,len(w)-1):
            sum+=w[i]
        return sum/(len(w)-2)

        