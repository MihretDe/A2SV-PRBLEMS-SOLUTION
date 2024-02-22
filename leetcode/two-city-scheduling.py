class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        diff_list =[]
        for a,b in costs:
            diff_list.append([b-a,a,b])
        diff_list.sort(reverse =True)
        total = 0
        for i in range(len(costs)):
            if i < len(costs)/2:
                total += diff_list[i][1]
            else:
                total += diff_list[i][2]
        return total
        
        



        