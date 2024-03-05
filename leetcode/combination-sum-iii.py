class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combination = []
        
        def order(i , path):
            if len(path) == k:
                if sum(path) == n:
                    combination. append(path[:])
                return 
            
            for j in range(i , 10):
                path.append(j)
                order(j+1 , path)
                path.pop()
        order(1,[])
        return combination
        