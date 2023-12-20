class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        converted_integer = int(''.join(map(str, digits)))
        converted_integer += 1
        converted_list = [int(digit) for digit in str(converted_integer)]
        return converted_list
