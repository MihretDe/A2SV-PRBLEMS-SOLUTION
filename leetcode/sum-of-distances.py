class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        count = defaultdict(list)
        for i in range(len(nums)):
            count[nums[i]].append(i)
        ans = [0]* len(nums)
        for i , val in count.items():
            suffix = sum(val)
            prefix = 0
            if len(val) == 1:
                continue 
            p = 0
            q = len(val)
            for ind in val:
                prefix += ind
                p+=1
                suffix -= ind
                q -=1 
                ans[ind] = (p*ind - prefix) + (suffix - (q * ind))
        return ans 
            
            


