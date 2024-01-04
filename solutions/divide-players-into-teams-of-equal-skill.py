class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left=0
        right=len(skill) - 1
        skill.sort()
        req=skill[left] + skill[right]
        ans = 0
        while left < right:
            if req!=skill[left] + skill[right]:
                return -1
            else:
                ans += skill[left] * skill[right]
                left +=1
                right -= 1
        return ans