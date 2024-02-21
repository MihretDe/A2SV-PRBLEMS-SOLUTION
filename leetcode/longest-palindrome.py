class Solution:
    def longestPalindrome(self, s: str) -> int:
        count  = Counter(s)
        count_list = list(count.values())
        count_list.sort(reverse =True)
        ans = 0
        found = False
        for i in range(len(count_list)):
            if count_list[i] %2 == 0:
                ans+=count_list[i]
            else:
                if found:
                    ans+=count_list[i]-1
                else:
                    ans+=count_list[i]
                    found=True

        return ans