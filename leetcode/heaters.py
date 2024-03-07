class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        next_heater = [-1] * len(houses)
        prev_heater = [-1] * len(houses)
        heaters.sort()
        for i in range(len(houses)):
            target = houses[i]
            left  = 0
            right = len(heaters) - 1
            ans = float(inf)
            while left <= right :
                mid = (left + right) // 2
                if heaters[mid] >= target:
                    ans = heaters[mid]
                    right = mid - 1
                else:
                    left = mid + 1
            if ans != float(inf):
                next_heater[i] = ans - houses[i]
        for i in range(len(houses)):
            target = houses[i]
            left  = 0
            right = len(heaters) - 1
            ans = float(inf)
            while left <= right :
                mid = (left + right) // 2
                if heaters[mid] <= target:
                    ans = heaters[mid]
                    left = mid + 1
                else:
                    right = mid - 1
            if ans != float(inf):
                prev_heater[i] = houses[i] - ans
        answer = []
        for i in range(len(next_heater)):
            if next_heater[i]== -1 or prev_heater[i]== -1:
                answer.append(max(next_heater[i] , prev_heater[i]))
            else:
                answer.append(min(next_heater[i] , prev_heater[i]))

        return max(answer)
            
            
