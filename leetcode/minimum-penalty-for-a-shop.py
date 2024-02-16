class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix =[0] * len(customers) 
        suffix = [0] * len(customers) 
        if customers[0]=='N':
            prefix[0] = 1
        for i in range(1,len(customers)):
            if customers[i]=='N':
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]
       
        if customers[-1] =='Y':
            suffix[0]=1
        j=1
        for i in range(len(customers) -2 , -1 , -1):
            if customers[i]=='Y':
                suffix[j] = suffix[j-1] + 1
            else:
                suffix[j] = suffix[j-1]
            j+=1
        suffix.reverse()
        suffix.append(0)
        prefix.reverse()
        prefix.append(0)
        prefix.reverse()
        ans = float('inf')
        r = -1
        for i in range(len(prefix)):
            if prefix[i] + suffix[i] < ans:
                r = i
                ans =  prefix[i] + suffix[i]

        return r

       

