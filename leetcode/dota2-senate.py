class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queueD = deque()
        queueR = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                queueR.append(i)
            else:
                queueD.append(i)
        print(queueD)
        print(queueR)
        
        while queueD and queueR:
            D = queueD.popleft()
            R = queueR.popleft()
            if D > R:
                queueR.append(R+len(senate))
            else:
                queueD.append(D+len(senate))
        
        if queueD:
            return "Dire"
        else:
            return "Radiant"


            
            

        