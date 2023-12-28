class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        array_num=[0]*101
        res=[]
        for num in nums:
            array_num[num] += 1
        for num in nums:
            res.append(sum(array_num[:num]))
        return res