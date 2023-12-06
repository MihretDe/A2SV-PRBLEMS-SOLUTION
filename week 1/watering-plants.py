class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total_steps = 0
        sum = 0
        for i in range(len(plants)):
            sum += plants[i]
            total_steps += 1
            if sum > capacity:
                total_steps += 2*i
                sum = plants[i]
        return total_steps

        