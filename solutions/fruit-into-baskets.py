class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        length = 0
        left = 0
        right = 0
        exist = {}
        while right < len(fruits):
            exist[fruits[right]] = exist.get(fruits[right] , 0) + 1
            if len(exist) > 2:
                while len(exist) > 2 and left < right:
                    exist[fruits[left]] -= 1
                    if exist[fruits[left]] == 0:
                        del exist[fruits[left]]
                    left += 1
            length = max(length , right - left+1)
            right +=1
        return length
            
                    