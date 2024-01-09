class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left = 0
        right = 0
        res=[]
        while left < len(firstList) and right < len(secondList):
            arr1=[]
            if firstList[left][1] >= secondList[right][0] and firstList[left][0] <= secondList[right][1]:
                arr1.append(max(firstList[left][0], secondList[right][0]))
                arr1.append(min(firstList[left][1], secondList[right][1]))
                res.append(arr1)
            if firstList[left][1] < secondList[right][1]:
                left += 1
            else:
                right += 1

        return res


