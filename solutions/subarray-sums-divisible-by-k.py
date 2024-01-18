class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count =0
        count1=defaultdict(int)
        prefix =[]
        pre = 0
        for i in range(0,len(nums)):
            pre+= nums[i]
            prefix.append(pre)
            if prefix[i] %  k == 0 :
                count +=1
            remainder = prefix[i] % k 
            if remainder < 0:
                remainder +=k
            if remainder  in count1:
                count += count1[remainder]
                

            count1[remainder]+=1
        return count 
                    