class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater_pivot = []
        result =[]
        for num in nums:
            if num < pivot:
                result.append(num)
            elif num > pivot:
                greater_pivot.append(num)
        for _ in range(nums.count(pivot)):
            result.append(pivot)
        result.extend(greater_pivot)
        return result


        