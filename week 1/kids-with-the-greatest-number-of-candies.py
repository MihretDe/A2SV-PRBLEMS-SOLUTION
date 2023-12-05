class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_a = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= max_a:
                result.append(True)
            else:
                result.append(False)
        return result

        