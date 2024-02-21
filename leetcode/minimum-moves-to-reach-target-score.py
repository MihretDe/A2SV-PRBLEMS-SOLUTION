class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        for i in range(maxDoubles):
            if target==1:
                break
            if target%2==1:
                ans+=1
            target=target//2
            ans+=1
            # if target==1:
            #     break
        ans += target-1
        return ans  