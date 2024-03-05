class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        def sets(indx , path):
            if sum(path) > target:
                return 
            for i in range(indx, len(candidates)):
                path.append(candidates[i])
                sets(i , path)
                if sum(path) == target:
                    subsets.append(path[:])
                path.pop()
        sets(0 ,[])
        return subsets