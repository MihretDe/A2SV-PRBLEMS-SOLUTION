class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ind = bisect_right(letters , target)
        if ind == len(letters):
            return letters[0]
        return letters[ind]