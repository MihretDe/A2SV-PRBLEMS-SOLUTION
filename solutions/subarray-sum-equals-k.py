class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =0
        count1=defaultdict(int)
        prefix =[]
        pre = 0
        for i in range(0,len(nums)):
            pre+= nums[i]
            prefix.append(pre)
            if prefix[i] == k:
                count +=1
           
            if prefix[i] -k in count1:
                count += count1[prefix[i] - k]
            count1[prefix[i]]+=1
            
        return count 
                    


            