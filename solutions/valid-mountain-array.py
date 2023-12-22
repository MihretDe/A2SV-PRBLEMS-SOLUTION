class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        flag=0
        exist = 0
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1]:
            return False
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                continue
            else:
                curr = i
                flag = 1
                break
        if flag == 0:
            return False
        else:
            for i in range(curr,len(arr)-1):
                if arr[i] > arr[i+1]:
                    continue
                else:
                    return False
        return True