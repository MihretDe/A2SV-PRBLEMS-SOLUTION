class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_tuple=[(s[0]**2 + s[1]**2, s) for s in points]
        dist_tuple.sort()
        return [point for _, point in dist_tuple[:k]]