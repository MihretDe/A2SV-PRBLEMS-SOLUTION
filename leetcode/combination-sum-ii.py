class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        subsets = []
        top = float(inf)
        # candidates.sort()
        def sets(indx , path , top):
            if sum(path) > target:
                return 
            for i in range(indx, len(candidates)):
                if top == candidates[i]:
                    continue
                path.append(candidates[i])
                sets(i+1 , path , top)
                if sum(path) == target:
                    for sub in subsets:
                        if Counter(sub) == Counter(path):
                            break
                    else:
                        subsets.append(path[:])
                top = path.pop()
        if sum(candidates) < target:
            return []
        sets(0 ,[] , top)
        return subsets