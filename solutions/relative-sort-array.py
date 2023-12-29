class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dict_nums=Counter(arr1)
        res=[]
        for num in arr2:
            res.extend([num]*dict_nums[num])
            del dict_nums[num]
        remain=[]
        for num, count in dict_nums.items():
            remain.extend([num] * count)
        res.extend(sorted(remain))
        return res

