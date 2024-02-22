class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i in range(len(tickets)):
            queue.append(i)
        time = 0
        while tickets[k] > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    queue.pop()
                    time+=1
                    if tickets[i] > 0:
                        queue.append(i)
                if i ==k and tickets[i]==0:
                    break
        return time





        # ans = 0
        # target = tickets[k]
        # for val in tickets:
        #     if val >= target:
        #         ans += target
        #     else:
        #         ans += val
        # return ans 

