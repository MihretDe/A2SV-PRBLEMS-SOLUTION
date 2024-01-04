class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # nums.sort(reverse=True)
        # operations = 0
        # n = len(nums)

        # for i in range(n - 1):
        #     largest = nums[i]
        #     next_largest = nums[i + 1]

        #     if largest > next_largest:
        #         operations += (i + 1) 

        # return operations
        operations = 0
        dict_nums=Counter(nums)
        sorted_nums=sorted(set(nums))
        n = len(sorted_nums)
        for i in range(n):
            operations+=i*dict_nums[sorted_nums[i]]
        return operations