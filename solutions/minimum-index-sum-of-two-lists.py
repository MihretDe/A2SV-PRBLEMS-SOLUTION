class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_list = []
        min_index = 2**31
        for word in list1:
            if word in list2:
                current_index = list1.index(word) + list2.index(word)
                if current_index < min_index:
                    common_list.clear()
                    common_list.append(word)
                    min_index = current_index
                elif current_index == min_index:
                    common_list.append(word)
        return common_list

        