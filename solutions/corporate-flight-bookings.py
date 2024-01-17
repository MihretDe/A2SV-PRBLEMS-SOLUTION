class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0] * (n+2)
        for booking in bookings:
            arr[booking[0]] += booking[2]
            arr[booking[1] + 1] -=booking[2]
        print(arr)
        
        prefix=[arr[0]]
        for i in range(1,len(arr)):
            prefix.append(prefix[i-1] + arr[i])
        return prefix[1:-1]
        