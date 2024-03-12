class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        for i in range(len(arr)):
            diff.append([abs(arr[i] - x) , arr[i]])
        diff.sort()
        ans = []
        for i in range(k):
            ans.append(diff[i][1])
        ans.sort()
        return ans 
