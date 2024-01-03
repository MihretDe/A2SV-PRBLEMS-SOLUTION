class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        k=len(tasks)//len(processorTime)
        i=0
        res=0
        for processor in processorTime:
            arr= [x + processor for x in tasks[i:i+k]]
            res=max(res,max(arr))
            i+=k
        return res

