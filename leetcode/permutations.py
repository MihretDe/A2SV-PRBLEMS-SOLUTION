class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def order(path):
            if len(path) == len(nums):
                permutations. append(path[:])
                return 
            
            for j in range(len(nums)):
                if nums[j] in path:
                    continue 
                path.append(nums[j])
                order(path)
                path.pop()

        order([])
        return permutations 