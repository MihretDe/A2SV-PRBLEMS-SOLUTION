class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        count= [0] * (max(costs) + 1)
        
        for cost in costs:
            count[cost] += 1
        
        total_cost = 0
        bars_bought = 0
        for cost in range(len(count)):
            while count[cost] > 0 and total_cost + cost <= coins:
                total_cost += cost
                count[cost] -= 1
                bars_bought += 1

        return bars_bought

        