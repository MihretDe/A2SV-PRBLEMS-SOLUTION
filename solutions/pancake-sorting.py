class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end=len(arr)
        res=[]
        if arr == sorted(arr):
            return res
        else:
            for _ in range(len(arr)):
                max_end = arr.index(end)+ 1
                if 1 <  max_end < end:
                    segment = arr[:max_end]
                    segment.reverse()
                    arr[:max_end]=segment
                    segment = arr[:end]
                    segment.reverse()
                    arr[:end]=segment
                    res.append(max_end)
                    res.append(end)
                elif max_end == 1:
                    segment = arr[:end]
                    segment.reverse()
                    arr[:end]=segment
                    res.append(end)
                end -= 1
        return res



                

        