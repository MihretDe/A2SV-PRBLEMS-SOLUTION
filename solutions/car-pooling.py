class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tu = [(arr[2], arr) for arr in trips]
        tu.sort(reverse=True)
        prefix = [0] * (tu[0][1][2] + 1) 
        for trip in trips:
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]
       
        prefix_sum =[prefix[0]]
        for i in range(1,len(prefix)):
            prefix_sum.append(prefix_sum[i-1] + prefix[i])
        
        if max(prefix_sum[:-1]) > capacity:
            return False
        else:
            return True

        