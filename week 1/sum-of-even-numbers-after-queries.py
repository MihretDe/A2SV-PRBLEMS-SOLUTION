class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums_dict = {}
        result = []
        even_sum = sum(num for num in nums if num % 2 == 0)

        for index, num in enumerate(nums):
            nums_dict[index] = num

        for query in queries:
            prev_value = nums_dict[query[1]]
            nums_dict[query[1]] += query[0]
            new_value = nums_dict[query[1]]

            if prev_value % 2 == 0:
                even_sum -= prev_value
            if new_value % 2 == 0:
                even_sum += new_value

            result.append(even_sum)

        return result
        
        
        