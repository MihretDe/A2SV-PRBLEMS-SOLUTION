class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed =[]
        for i in range(len(nums)):
            if i%2==0:
                for _ in range(nums[i]):
                    decompressed.append(nums[i+1])
        return decompressed

