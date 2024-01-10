class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited=set()
        for i in range(len(nums)):
            loop=set()
            if i not in visited:
                while True:
                    if i in loop:
                        return True
                    visited.add(i)
                    loop.add(i)
                    prev , i=i,(i+nums[i])%len(nums)
                    if prev== i:
                        break
                    if nums[prev] * nums[i] < 0 :
                        break
        return False 