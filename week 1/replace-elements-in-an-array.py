class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        '''for operation in operations:
            new_val = operation[1]
            to_replaced = operation[0]
            nums[nums.index(to_replaced)] = new_val
        return nums'''
        nums_dict = {num: i for i, num in enumerate(nums)}
        for operation in operations:
            index = nums_dict[operation[0]]
            nums[index] = operation[1]
            nums_dict[operation[1]] = index
            del nums_dict[operation[0]]
        return nums
