class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_val=max(heights)
        array = [0]* (max_val+1)
        dict_height={}
        for i in range(len(heights)):
            dict_height[heights[i]]=names[i]
        for num in heights:
            array[num] += 1
        array2=[]
        for i in range(len(array)):
            if array[i] > 0:
                array3=[i]*array[i]
                array2.extend(array3)
        res=[]
        for i in range(len(heights)-1,-1,-1):
            res.append(dict_height[array2[i]])
        return res
        