class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count_arr = Counter(arr)
        quarter = len(arr) // 4
        for num,cou in count_arr.items():
            if cou > quarter:
                return num
        