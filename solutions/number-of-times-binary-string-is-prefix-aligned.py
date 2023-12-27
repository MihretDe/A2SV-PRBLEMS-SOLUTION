class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        binary=[0]*len(flips)
        count=0
        dict_1={1:0}
        ones=0
        for i in range(len(flips)):
            binary[flips[i]-1]=1
            # if binary[:i+1] == [1]*(i+1):
            #         count += 1
            if flips[i]-1 < i:
                ones +=1
            if binary[i]==1:
                ones +=1
            if ones==i+1:
                count += 1


            

        return count
        
