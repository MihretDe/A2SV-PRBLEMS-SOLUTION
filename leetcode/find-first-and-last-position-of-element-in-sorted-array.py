class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        position = [-1 , -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] < target:
                left  = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                position[0] = mid
                right = mid -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) //2
            if nums[mid] < target:
                left  = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                position[1] = mid
                left = mid + 1
        

                
        return position

