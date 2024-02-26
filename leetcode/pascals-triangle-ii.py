class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        result = self.getRow(rowIndex - 1)

        prefix = [result[0]]
        middle = result[len(result)//2 - 1]
        for i in range(1 ,ceil( len(result)/2)):
            prefix.append(result[i-1] + result[i])
        if rowIndex % 2 == 0:
            prefix.append(middle * 2)
        n =len(prefix)
        if rowIndex % 2 == 0:
            for i in range(len(prefix) -2 , -1 ,-1):
                prefix.append(prefix[i])
        else:
            for i in range(len(prefix) -1 , -1 ,-1):
                prefix.append(prefix[i])

        return prefix




        