class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count =0
        count1=defaultdict(int)
        prefix =[]
        pre = 0
        for i in range(0,len(nums)):
            pre+= nums[i]
            prefix.append(pre)
            if prefix[i] == goal:
                count +=1
           
            if prefix[i] -goal in count1:
                count += count1[prefix[i] - goal]
            count1[prefix[i]]+=1
            
        return count

