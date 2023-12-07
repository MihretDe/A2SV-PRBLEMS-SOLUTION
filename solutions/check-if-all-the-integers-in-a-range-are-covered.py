class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
       # ranges_set = set(ranges)
      ranges_set = set()


      for i in range(len(ranges)):
        ranges_set.update(j for j in range(ranges[i][0], ranges[i][1]+1))
      for i in range (left,right+1):
        if i not in ranges_set:
          return False
      return True

        