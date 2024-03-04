class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        def sets(indx , path):
            if len(subsets) == 2 ** len(nums):
                return
            for i in range(indx , len(nums)):
                path.append(nums[i])
                sets(i+1 , path)
                subsets.append(path[:])
                path.pop()
        sets(0 ,[])
        return subsets
        
                






