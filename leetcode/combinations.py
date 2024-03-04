class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combination = []
        
        def order(i , path):
            if len(path) == k:
                combination. append(path[:])
                return 
            
            for j in range(i , n+1):
                path.append(j)
                order(j+1 , path)
                path.pop()

        order(1 , [])
        return combination 

        
